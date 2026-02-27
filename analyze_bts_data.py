#!/usr/bin/env python3
"""
Download and process Bureau of Transportation Statistics (BTS) T-100 data
for flights to/from Kotzebue Airport (OTZ).

This is a more reliable alternative to OpenSky for commercial flight data.
"""

import pandas as pd
from datetime import datetime
import os


def load_bts_t100_data(filepath: str) -> pd.DataFrame:
    """
    Load and process BTS T-100 data from a CSV file.
    
    The T-100 data can be downloaded from:
    https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD
    
    Args:
        filepath: Path to the downloaded CSV file
        
    Returns:
        Processed DataFrame
    """
    print(f"Loading BTS T-100 data from: {filepath}")
    
    try:
        df = pd.read_csv(filepath)
        print(f"✓ Loaded {len(df)} records")
        return df
    except FileNotFoundError:
        print(f"✗ File not found: {filepath}")
        print("\nTo download T-100 data:")
        print("1. Visit: https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD")
        print("2. Select 'T-100 Domestic Segment (U.S. Carriers)'")
        print("3. Filter by:")
        print("   - Origin or Dest: OTZ")
        print("   - Year: 2019-2025")
        print("   - All available fields")
        print("4. Download as CSV")
        return pd.DataFrame()
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        return pd.DataFrame()


def filter_otz_arrivals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter for flights arriving at OTZ.
    
    Args:
        df: Raw BTS T-100 DataFrame
        
    Returns:
        Filtered DataFrame with arrivals to OTZ
    """
    if df.empty:
        return df
    
    # Common column names in T-100 data
    dest_cols = ['DEST', 'Dest', 'DEST_AIRPORT_ID', 'DestAirportID']
    
    dest_col = None
    for col in dest_cols:
        if col in df.columns:
            dest_col = col
            break
    
    if dest_col is None:
        print("✗ Could not find destination column in data")
        print(f"Available columns: {df.columns.tolist()}")
        return pd.DataFrame()
    
    arrivals = df[df[dest_col] == 'OTZ'].copy()
    print(f"\n✓ Found {len(arrivals)} arrival records to OTZ")
    
    return arrivals


def analyze_otz_flights(df: pd.DataFrame):
    """
    Analyze and summarize OTZ flight data.
    
    Args:
        df: DataFrame with OTZ flight data
    """
    if df.empty:
        print("No data to analyze")
        return
    
    print("\n" + "="*60)
    print("OTZ ARRIVALS ANALYSIS")
    print("="*60)
    
    # Identify key columns
    year_col = 'YEAR' if 'YEAR' in df.columns else 'Year'
    month_col = 'MONTH' if 'MONTH' in df.columns else 'Month'
    carrier_col = next((c for c in ['UNIQUE_CARRIER', 'UniqueCarrier', 'CARRIER'] if c in df.columns), None)
    origin_col = next((c for c in ['ORIGIN', 'Origin', 'ORIGIN_AIRPORT_ID'] if c in df.columns), None)
    
    # Flights column - could be DEPARTURES_PERFORMED or similar
    flights_col = next((c for c in ['DEPARTURES_PERFORMED', 'Departures', 'FLIGHTS'] if c in df.columns), None)
    passengers_col = next((c for c in ['PASSENGERS', 'Passengers', 'PAX'] if c in df.columns), None)
    
    if year_col and year_col in df.columns:
        print(f"\nFlights by Year:")
        if flights_col and flights_col in df.columns:
            yearly = df.groupby(year_col)[flights_col].sum().sort_index()
            for year, count in yearly.items():
                print(f"  {year}: {count:,.0f} flights")
        else:
            yearly = df[year_col].value_counts().sort_index()
            for year, count in yearly.items():
                print(f"  {year}: {count:,.0f} records")
    
    if carrier_col and carrier_col in df.columns:
        print(f"\nTop Airlines:")
        if flights_col and flights_col in df.columns:
            carriers = df.groupby(carrier_col)[flights_col].sum().sort_values(ascending=False)
            for carrier, count in carriers.head(10).items():
                print(f"  {carrier}: {count:,.0f} flights")
        else:
            carriers = df[carrier_col].value_counts()
            for carrier, count in carriers.head(10).items():
                print(f"  {carrier}: {count:,.0f} records")
    
    if origin_col and origin_col in df.columns:
        print(f"\nTop Origin Airports:")
        if flights_col and flights_col in df.columns:
            origins = df.groupby(origin_col)[flights_col].sum().sort_values(ascending=False)
            for origin, count in origins.head(10).items():
                print(f"  {origin}: {count:,.0f} flights")
        else:
            origins = df[origin_col].value_counts()
            for origin, count in origins.head(10).items():
                print(f"  {origin}: {count:,.0f} records")
    
    if passengers_col and passengers_col in df.columns:
        print(f"\nPassenger Statistics:")
        total_pax = df[passengers_col].sum()
        print(f"  Total passengers: {total_pax:,.0f}")
        
        if year_col in df.columns:
            print(f"  Passengers by year:")
            yearly_pax = df.groupby(year_col)[passengers_col].sum().sort_index()
            for year, pax in yearly_pax.items():
                print(f"    {year}: {pax:,.0f}")
    
    print(f"\nData columns available:")
    for col in df.columns:
        print(f"  - {col}")


def main():
    """Main execution function."""
    print("BTS T-100 Data Analyzer for Kotzebue Airport (OTZ)")
    print("="*60)
    print()
    
    # Check for data file
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    
    # Look for CSV files in data directory
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in data/ directory")
        print("\nINSTRUCTIONS TO DOWNLOAD DATA:")
        print("="*60)
        print("1. Visit: https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD")
        print("2. Click on 'T-100 Domestic Segment (U.S. Carriers)'")
        print("3. Configure your download:")
        print("   - Geography: Select 'Origin or Dest' = OTZ")
        print("   - Time Period: Select years 2019-2025")
        print("   - Data Type: Select all available fields")
        print("4. Download as CSV")
        print("5. Save the file to the 'data/' directory")
        print("6. Run this script again")
        print()
        print("Alternatively, you can also download:")
        print("- T-100 Domestic Market data")
        print("- Passenger and freight statistics")
        return
    
    print(f"Found {len(csv_files)} CSV file(s) in data/ directory:")
    for i, f in enumerate(csv_files, 1):
        print(f"  {i}. {f}")
    
    # Use the first CSV file
    filepath = os.path.join(data_dir, csv_files[0])
    print(f"\nUsing: {filepath}")
    print()
    
    # Load and process data
    df = load_bts_t100_data(filepath)
    
    if not df.empty:
        # Filter for OTZ arrivals
        arrivals = filter_otz_arrivals(df)
        
        if not arrivals.empty:
            # Analyze the data
            analyze_otz_flights(arrivals)
            
            # Save processed data
            output_file = os.path.join(data_dir, f"otz_arrivals_processed_{datetime.now().strftime('%Y%m%d')}.csv")
            arrivals.to_csv(output_file, index=False)
            print(f"\n✓ Processed data saved to: {output_file}")


if __name__ == '__main__':
    main()
