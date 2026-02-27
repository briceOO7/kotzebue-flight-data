# OpenSky Flight Data Collector for Kotzebue, AK (OTZ)

This project collects historical flight arrival data for Kotzebue Airport (OTZ) from 2019-2025 using the OpenSky Network API.

## Overview

The OpenSky Network provides free access to flight data, but with some limitations:
- Maximum 7-day intervals for airport arrival/departure queries
- Anonymous requests limited to one per 10 seconds
- Authenticated requests have higher rate limits

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Collect Flight Data

Run the main collector script to gather all arrivals to OTZ:

```bash
python collect_otz_flights.py
```

This will:
- Query arrivals to OTZ airport in 7-day intervals from 2019-2025
- Save data to CSV files in the `data/` directory
- Include a 10-second delay between requests (API rate limit)
- Create a combined dataset of all flights

### Configuration

Edit `collect_otz_flights.py` to:
- Set OpenSky credentials (optional, for higher rate limits)
- Adjust date range
- Modify output format

## Data Structure

The collected data includes:
- ICAO24 address (aircraft identifier)
- Callsign
- Departure airport (estimated)
- Arrival airport (OTZ)
- First seen time (departure)
- Last seen time (arrival)
- Distance metrics

## Notes

- The ICAO code for Kotzebue Airport is "PAOT"
- Data collection for 6 years will take significant time due to API rate limits
- Expected time: ~300+ API calls × 10 seconds = ~50+ minutes for full dataset
