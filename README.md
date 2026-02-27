# OpenSky Flight Data Collector for Kotzebue, AK (OTZ)

This project attempts to collect historical flight arrival data for Kotzebue Airport (OTZ/PAOT) from 2019-2025 using the OpenSky Network API.

## ⚠️ Important Limitations

After testing, we've discovered several important limitations:

1. **OpenSky API Rate Limits**: The OpenSky Network has very strict rate limits:
   - Anonymous users: Very limited access, easily blocked
   - Authenticated users: Better limits but still restricted
   - They may block certain cloud providers and IP ranges

2. **Small Airport Coverage**: OpenSky relies on ADS-B receivers. Remote airports like Kotzebue may have:
   - Limited or no ADS-B receiver coverage
   - Few ADS-B-equipped aircraft
   - Incomplete historical data

3. **API Status**: As of testing (Feb 2026), the OpenSky flights API returned 403 errors, suggesting access restrictions or rate limiting.

## Alternative Data Sources

For comprehensive flight data to Kotzebue Airport, consider these alternatives:

### 1. **FAA Data Sources** (Free, US Government)
- **ASPM (Aviation System Performance Metrics)**: https://aspm.faa.gov/
- **TFM Data**: Through FAA System Wide Information Management (SWIM)
- **Bureau of Transportation Statistics**: https://www.transtats.bts.gov/

### 2. **FlightAware** (Commercial API)
- Better coverage of small US airports
- Historical data available
- Commercial pricing
- API: https://flightaware.com/commercial/firehose/

### 3. **Alaska-Specific Sources**
- **Alaska DOT&PF Aviation Division**: May have traffic records
- **Air Carriers**: Contact airlines serving OTZ directly:
  - Alaska Airlines
  - Bering Air
  - Ravn Alaska
  - Grant Aviation

### 4. **Bureau of Transportation Statistics (BTS)**
- **T-100 Domestic Segment Data**: Monthly air carrier statistics
- Includes passenger counts, flights, by route
- Free download: https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD

## Installation

If you want to try the OpenSky API (requires authentication):

```bash
pip install -r requirements.txt
```

## Usage

### Test API Access

First, test if you can access the OpenSky API:

```bash
# Without authentication (very limited)
python test_api.py

# With authentication (register at https://opensky-network.org/)
export OPENSKY_USERNAME="your_username"
export OPENSKY_PASSWORD="your_password"
python test_api_comprehensive.py
```

### Collect Flight Data (if API access works)

```bash
python collect_otz_flights.py
```

This will:
- Query arrivals to PAOT airport in 7-day intervals from 2019-2025
- Save data to CSV files in the `data/` directory
- Include rate-limiting delays between requests
- Create a combined dataset of all flights

### Configuration

Edit `collect_otz_flights.py` to:
- Set OpenSky credentials (required for any meaningful access)
- Adjust date range
- Modify output format

## Data Structure

If data is collected, it includes:
- ICAO24 address (aircraft identifier)
- Callsign
- Departure airport (estimated)
- Arrival airport (PAOT)
- First seen time (departure)
- Last seen time (arrival)
- Distance metrics

## Recommended Approach: BTS T-100 Data

The most reliable source for commercial flight data to OTZ is the **Bureau of Transportation Statistics T-100 data**:

1. Visit: https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD&QO_anzr=Nv4%20Pn44vr45%20G-100%20Qbzr5gvp%20Fr tzrag%20(H.F.%20Pn44vr45)
2. Filter by destination: OTZ
3. Select date range: 2019-2025
4. Download as CSV

This will give you:
- All commercial air carrier flights
- Passenger counts
- Freight data
- Monthly summaries
- 100% accurate and complete for scheduled commercial service

## Notes

- The ICAO code for Kotzebue Airport is "PAOT"
- The IATA code is "OTZ"
- Kotzebue is a remote Arctic Circle airport with limited service
- Most flights are regional carriers with smaller aircraft
