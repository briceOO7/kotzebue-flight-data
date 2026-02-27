#!/usr/bin/env python3
"""
Collect flight arrival data for Kotzebue Airport (PAOT) from 2019-2025
using the OpenSky Network API.
"""

import os
import time
from datetime import datetime, timedelta
from typing import Optional
import pandas as pd
from opensky_api import OpenSkyApi


class OTZFlightCollector:
    """Collector for flight data to Kotzebue Airport (PAOT)."""
    
    AIRPORT_ICAO = "PAOT"
    
    def __init__(self, username: Optional[str] = None, password: Optional[str] = None):
        """
        Initialize the collector.
        
        Args:
            username: OpenSky username (optional, for higher rate limits)
            password: OpenSky password (optional)
        """
        self.api = OpenSkyApi(username, password)
        self.is_authenticated = username is not None
        self.delay_seconds = 1 if self.is_authenticated else 10
        
    def collect_arrivals(self, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        """
        Collect all arrivals to OTZ between start_date and end_date.
        
        The API limits queries to 7-day intervals, so this method breaks the
        request into multiple chunks.
        
        Args:
            start_date: Start of collection period (datetime)
            end_date: End of collection period (datetime)
            
        Returns:
            DataFrame with all collected flight data
        """
        all_flights = []
        current_start = start_date
        interval_days = 7
        
        total_days = (end_date - start_date).days
        num_intervals = (total_days // interval_days) + 1
        
        print(f"Collecting arrivals from {start_date.date()} to {end_date.date()}")
        print(f"This will require approximately {num_intervals} API calls")
        print(f"Estimated time: {num_intervals * self.delay_seconds / 60:.1f} minutes\n")
        
        interval_count = 0
        
        while current_start < end_date:
            current_end = min(current_start + timedelta(days=interval_days), end_date)
            
            begin_ts = int(current_start.timestamp())
            end_ts = int(current_end.timestamp())
            
            interval_count += 1
            print(f"[{interval_count}/{num_intervals}] Fetching {current_start.date()} to {current_end.date()}...", end=" ")
            
            try:
                flights = self.api.get_arrivals_by_airport(
                    self.AIRPORT_ICAO,
                    begin_ts,
                    end_ts
                )
                
                if flights:
                    flight_count = len(flights)
                    print(f"✓ Found {flight_count} flights")
                    
                    for flight in flights:
                        all_flights.append({
                            'icao24': flight.icao24,
                            'callsign': flight.callsign.strip() if flight.callsign else None,
                            'departure_airport': flight.estDepartureAirport,
                            'arrival_airport': flight.estArrivalAirport,
                            'first_seen': flight.firstSeen,
                            'last_seen': flight.lastSeen,
                            'first_seen_datetime': datetime.fromtimestamp(flight.firstSeen) if flight.firstSeen else None,
                            'last_seen_datetime': datetime.fromtimestamp(flight.lastSeen) if flight.lastSeen else None,
                            'departure_distance_horiz': flight.estDepartureAirportHorizDistance,
                            'departure_distance_vert': flight.estDepartureAirportVertDistance,
                            'arrival_distance_horiz': flight.estArrivalAirportHorizDistance,
                            'arrival_distance_vert': flight.estArrivalAirportVertDistance,
                            'departure_candidates': flight.departureAirportCandidatesCount,
                            'arrival_candidates': flight.arrivalAirportCandidatesCount,
                        })
                else:
                    print("✓ No flights found")
                    
            except Exception as e:
                print(f"✗ Error: {e}")
                
            current_start = current_end
            
            if current_start < end_date:
                time.sleep(self.delay_seconds)
        
        if all_flights:
            df = pd.DataFrame(all_flights)
            df = df.sort_values('last_seen')
            return df
        else:
            return pd.DataFrame()
    
    def save_to_csv(self, df: pd.DataFrame, filename: str):
        """Save DataFrame to CSV file."""
        os.makedirs('data', exist_ok=True)
        filepath = os.path.join('data', filename)
        df.to_csv(filepath, index=False)
        print(f"\n✓ Data saved to {filepath}")
        print(f"  Total flights: {len(df)}")
        if len(df) > 0:
            print(f"  Date range: {df['first_seen_datetime'].min()} to {df['last_seen_datetime'].max()}")
            print(f"  Unique aircraft: {df['icao24'].nunique()}")
            if df['departure_airport'].notna().any():
                print(f"  Unique departure airports: {df['departure_airport'].nunique()}")


def main():
    """Main execution function."""
    
    # Optional: Set credentials for authenticated access (higher rate limits)
    username = os.environ.get('OPENSKY_USERNAME')
    password = os.environ.get('OPENSKY_PASSWORD')
    
    if username:
        print("Using authenticated access (faster rate limits)")
    else:
        print("Using anonymous access (10 second delay between requests)")
        print("Set OPENSKY_USERNAME and OPENSKY_PASSWORD environment variables for faster access\n")
    
    collector = OTZFlightCollector(username, password)
    
    # Define collection period
    start_date = datetime(2019, 1, 1)
    end_date = datetime(2025, 12, 31, 23, 59, 59)
    
    # Collect the data
    df = collector.collect_arrivals(start_date, end_date)
    
    if not df.empty:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'otz_arrivals_2019_2025_{timestamp}.csv'
        collector.save_to_csv(df, filename)
        
        print("\n" + "="*60)
        print("Summary Statistics:")
        print("="*60)
        
        if 'departure_airport' in df.columns:
            print("\nTop departure airports:")
            print(df['departure_airport'].value_counts().head(10))
        
        if 'callsign' in df.columns and df['callsign'].notna().any():
            print("\nTop callsigns:")
            print(df['callsign'].value_counts().head(10))
        
        df['year'] = pd.to_datetime(df['last_seen_datetime']).dt.year
        print("\nFlights per year:")
        print(df['year'].value_counts().sort_index())
        
    else:
        print("\n✗ No flight data collected")


if __name__ == '__main__':
    main()
