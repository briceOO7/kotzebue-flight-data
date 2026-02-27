#!/usr/bin/env python3
"""
Comprehensive test script to check OpenSky API and PAOT availability.
"""

import os
from datetime import datetime, timedelta
import requests
from requests.auth import HTTPBasicAuth


def test_airport(airport_code, airport_name, begin, end, auth=None):
    """Test API with a specific airport."""
    url = "https://opensky-network.org/api/flights/arrival"
    
    params = {
        'airport': airport_code,
        'begin': int(begin.timestamp()),
        'end': int(end.timestamp())
    }
    
    print(f"\n{'='*60}")
    print(f"Testing: {airport_name} ({airport_code})")
    print(f"Period: {begin.date()} to {end.date()}")
    print(f"{'='*60}")
    
    try:
        response = requests.get(url, params=params, auth=auth, timeout=30)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            flights = response.json()
            count = len(flights) if flights else 0
            print(f"✓ Success - Found {count} arrivals")
            
            if flights and count > 0:
                print("\nSample flight:")
                f = flights[0]
                print(f"  ICAO24: {f.get('icao24')}")
                print(f"  Callsign: {f.get('callsign', '').strip()}")
                print(f"  From: {f.get('estDepartureAirport', 'Unknown')}")
                print(f"  Time: {datetime.fromtimestamp(f.get('lastSeen', 0))}")
            
            return count
        else:
            print(f"✗ Failed - {response.status_code}")
            if response.status_code == 404:
                print("  (Airport not found or no data available)")
            return 0
            
    except Exception as e:
        print(f"✗ Error: {e}")
        return 0


def main():
    """Run comprehensive tests."""
    print("OpenSky API Comprehensive Test")
    print("=" * 60)
    
    username = os.environ.get('OPENSKY_USERNAME')
    password = os.environ.get('OPENSKY_PASSWORD')
    auth = HTTPBasicAuth(username, password) if username else None
    
    if username:
        print(f"✓ Using authenticated access: {username}")
    else:
        print("⚠ Using anonymous access")
        print("  Set OPENSKY_USERNAME and OPENSKY_PASSWORD for better results")
    
    # Test periods
    now = datetime.now()
    recent = (now - timedelta(days=7), now)
    one_month_ago = (now - timedelta(days=30), now - timedelta(days=23))
    one_year_ago = (now - timedelta(days=365), now - timedelta(days=358))
    
    # Test 1: Major airport (should definitely work)
    print("\n" + "="*60)
    print("TEST 1: Major Airport (Validation)")
    test_airport("KSEA", "Seattle-Tacoma Intl", recent[0], recent[1], auth)
    
    # Wait to respect rate limit
    print("\nWaiting 10 seconds (rate limit)...")
    import time
    time.sleep(10)
    
    # Test 2: PAOT - Recent data
    print("\n" + "="*60)
    print("TEST 2: Kotzebue (PAOT) - Recent Data")
    count = test_airport("PAOT", "Ralph Wien Memorial", recent[0], recent[1], auth)
    
    if count == 0:
        print("\nNo recent data. Trying older periods...")
        
        time.sleep(10)
        
        # Test 3: PAOT - 1 month ago
        print("\n" + "="*60)
        print("TEST 3: Kotzebue (PAOT) - 1 Month Ago")
        count = test_airport("PAOT", "Ralph Wien Memorial", one_month_ago[0], one_month_ago[1], auth)
        
        if count == 0:
            time.sleep(10)
            
            # Test 4: PAOT - 1 year ago
            print("\n" + "="*60)
            print("TEST 4: Kotzebue (PAOT) - 1 Year Ago")
            test_airport("PAOT", "Ralph Wien Memorial", one_year_ago[0], one_year_ago[1], auth)
    
    # Test 5: Try nearby Alaskan airports
    print("\n\n" + "="*60)
    print("TEST 5: Other Alaska Airports (for comparison)")
    print("="*60)
    
    alaska_airports = [
        ("PANC", "Anchorage Intl"),
        ("PAFA", "Fairbanks Intl"),
        ("PABR", "Barrow/Utqiagvik"),
    ]
    
    for code, name in alaska_airports:
        time.sleep(10)
        test_airport(code, name, recent[0], recent[1], auth)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print("""
If PAOT shows 404 or 0 flights across all time periods:
- OpenSky may not have good coverage for this remote airport
- The airport may not have ADS-B equipped aircraft
- Historical data may not be available for small regional airports

Alternative approaches:
1. Use FAA ASPM (Aviation System Performance Metrics) data
2. Contact Alaska DOT for flight records
3. Use FlightAware API (commercial, better small airport coverage)
4. Check with air carriers serving OTZ (Alaska Airlines, Bering Air, Ravn Alaska)
    """)


if __name__ == '__main__':
    main()
