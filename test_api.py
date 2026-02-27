#!/usr/bin/env python3
"""
Test script to verify OpenSky API access and check if PAOT data is available.
"""

import os
from datetime import datetime, timedelta
import requests
from requests.auth import HTTPBasicAuth


def test_api_connection():
    """Test basic API connectivity and authentication."""
    print("Testing OpenSky API connection...\n")
    
    username = os.environ.get('OPENSKY_USERNAME')
    password = os.environ.get('OPENSKY_PASSWORD')
    
    auth = HTTPBasicAuth(username, password) if username else None
    
    if username:
        print(f"✓ Using authenticated access with username: {username}")
    else:
        print("⚠ Using anonymous access (slower, limited to 10 sec between requests)")
    
    print()
    
    url = "https://opensky-network.org/api/flights/arrival"
    
    # Test with a short time period
    end = datetime.now()
    begin = end - timedelta(hours=2)
    
    params = {
        'airport': 'PAOT',
        'begin': int(begin.timestamp()),
        'end': int(end.timestamp())
    }
    
    print(f"Testing with PAOT (Kotzebue Airport)")
    print(f"Time range: {begin} to {end} (last 2 hours)\n")
    
    try:
        response = requests.get(url, params=params, auth=auth, timeout=30)
        print(f"Status code: {response.status_code}")
        
        if response.status_code == 200:
            flights = response.json()
            print(f"✓ API call successful!")
            print(f"Flights found: {len(flights) if flights else 0}")
            
            if flights:
                print("\nSample flight data:")
                print(f"  ICAO24: {flights[0].get('icao24')}")
                print(f"  Callsign: {flights[0].get('callsign')}")
                print(f"  Departure: {flights[0].get('estDepartureAirport')}")
                print(f"  Arrival: {flights[0].get('estArrivalAirport')}")
            else:
                print("\nNo flights in the last 2 hours.")
                print("Trying a longer time period (7 days)...\n")
                
                # Try 7 days
                begin = end - timedelta(days=7)
                params['begin'] = int(begin.timestamp())
                
                response = requests.get(url, params=params, auth=auth, timeout=30)
                flights = response.json()
                
                print(f"Flights found (last 7 days): {len(flights) if flights else 0}")
                
                if flights:
                    print("\nSample flight data:")
                    print(f"  ICAO24: {flights[0].get('icao24')}")
                    print(f"  Callsign: {flights[0].get('callsign')}")
                    print(f"  Departure: {flights[0].get('estDepartureAirport')}")
                    print(f"  Arrival: {flights[0].get('estArrivalAirport')}")
        
        elif response.status_code == 401:
            print("✗ Authentication failed. Check your credentials.")
        
        elif response.status_code == 404:
            print("✗ Airport not found or no data available.")
            print("Note: PAOT is the ICAO code for Kotzebue Airport.")
            
        else:
            print(f"✗ Unexpected status code: {response.status_code}")
            print(f"Response: {response.text[:200]}")
    
    except requests.exceptions.Timeout:
        print("✗ Request timed out")
    
    except requests.exceptions.RequestException as e:
        print(f"✗ Request failed: {e}")


if __name__ == '__main__':
    test_api_connection()
