#!/usr/bin/env python3
"""
Helper script to generate direct download links and instructions for BTS data.
"""

import webbrowser


def print_instructions():
    """Print detailed instructions for accessing BTS data."""
    
    print("="*70)
    print("HOW TO GET FLIGHT DATA FOR KOTZEBUE AIRPORT (OTZ)")
    print("="*70)
    print()
    
    print("METHOD 1: BTS T-100 Data (RECOMMENDED)")
    print("-" * 70)
    print()
    print("The Bureau of Transportation Statistics provides comprehensive data")
    print("on all commercial flights in the United States.")
    print()
    print("Step 1: Go to BTS Database")
    print("  URL: https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD")
    print()
    print("Step 2: Select Dataset")
    print("  - Click 'T-100 Domestic Segment (U.S. Carriers)'")
    print("  - This includes all scheduled commercial flights")
    print()
    print("Step 3: Filter Data")
    print("  Geography:")
    print("    - Origin or Destination: OTZ")
    print("    - Or specifically: Destination = OTZ (for arrivals only)")
    print()
    print("  Time Period:")
    print("    - Year: Select 2019, 2020, 2021, 2022, 2023, 2024, 2025")
    print("    - Month: Select all months")
    print()
    print("  Variables (select all that interest you):")
    print("    ☑ DEPARTURES_PERFORMED (number of flights)")
    print("    ☑ PASSENGERS")
    print("    ☑ FREIGHT")
    print("    ☑ MAIL")
    print("    ☑ UNIQUE_CARRIER (airline code)")
    print("    ☑ ORIGIN")
    print("    ☑ DEST")
    print("    ☑ AIRCRAFT_TYPE")
    print()
    print("Step 4: Download")
    print("  - Select download format: CSV")
    print("  - Save to the 'data/' folder in this project")
    print()
    
    print("\nMETHOD 2: BTS On-Time Performance Data")
    print("-" * 70)
    print()
    print("For individual flight details:")
    print("  URL: https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ")
    print()
    print("  This includes:")
    print("    - Specific flight numbers")
    print("    - Actual departure/arrival times")
    print("    - Delays and cancellations")
    print("    - Tail numbers")
    print()
    print("  Filter by:")
    print("    - Origin or Destination: OTZ")
    print("    - Date range: 2019-2025")
    print()
    
    print("\nMETHOD 3: FAA Airport Data")
    print("-" * 70)
    print()
    print("FAA provides operational data:")
    print("  - ASPM: https://aspm.faa.gov/")
    print("  - Airport operations, delays, traffic counts")
    print()
    
    print("\nMETHOD 4: FlightAware (Commercial)")
    print("-" * 70)
    print()
    print("For real-time and historical flight tracking:")
    print("  - Website: https://flightaware.com/live/airport/PAOT")
    print("  - API: https://flightaware.com/commercial/aeroapi/")
    print("  - Better coverage than OpenSky for US regional airports")
    print("  - Requires paid subscription for API access")
    print()
    
    print("\nMETHOD 5: Contact Airlines Directly")
    print("-" * 70)
    print()
    print("Airlines serving Kotzebue (OTZ):")
    print("  1. Alaska Airlines")
    print("     - Main carrier for OTZ")
    print("     - Routes: Anchorage-Kotzebue, Fairbanks-Kotzebue")
    print()
    print("  2. Bering Air")
    print("     - Regional carrier")
    print("     - Website: https://beringair.com/")
    print()
    print("  3. Ravn Alaska")
    print("     - Regional carrier")
    print("     - Website: https://ravnalaska.com/")
    print()
    print("  4. Grant Aviation")
    print("     - Regional cargo and passenger service")
    print()
    
    print("\n" + "="*70)
    print("NEXT STEPS")
    print("="*70)
    print()
    print("1. Download BTS T-100 data following Method 1 above")
    print("2. Save the CSV file to the 'data/' folder")
    print("3. Run: python analyze_bts_data.py")
    print()
    print("The analysis script will:")
    print("  ✓ Load your downloaded data")
    print("  ✓ Filter for OTZ arrivals")
    print("  ✓ Generate statistics by year, airline, origin")
    print("  ✓ Calculate total flights and passengers")
    print("  ✓ Save processed results")
    print()


def open_bts_website():
    """Open the BTS website in default browser."""
    url = "https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD"
    print(f"\nOpening BTS website: {url}")
    try:
        webbrowser.open(url)
        print("✓ Browser opened")
    except Exception as e:
        print(f"Could not open browser: {e}")
        print(f"Please manually visit: {url}")


def main():
    """Main execution."""
    print_instructions()
    
    response = input("\nWould you like to open the BTS website now? (y/n): ")
    if response.lower().strip() in ['y', 'yes']:
        open_bts_website()
    else:
        print("\nYou can manually visit:")
        print("https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD")
    
    print("\n✓ Done. Download your data and run: python analyze_bts_data.py")


if __name__ == '__main__':
    main()
