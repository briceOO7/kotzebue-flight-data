# Quick Reference: Getting OTZ Flight Data

## TL;DR - Best Approach

1. Run: `python get_bts_data.py` (shows instructions)
2. Download CSV from BTS website
3. Run: `python analyze_bts_data.py` (analyzes your data)

## Why Not OpenSky?

The OpenSky Network API has severe limitations:
- ❌ 403 Forbidden errors (rate limiting/blocking)
- ❌ Limited coverage of remote Alaska airports
- ❌ Requires ADS-B receivers near airport
- ❌ Historical data may be incomplete

## Best Data Sources for OTZ

### 🥇 #1: BTS T-100 Data (FREE & COMPREHENSIVE)

**What you get:**
- ALL commercial flights 2019-2025
- Monthly statistics
- Passenger counts
- Freight data
- 100% complete for scheduled carriers

**How to get it:**
```bash
python get_bts_data.py  # Shows detailed instructions
```

Or visit directly:
https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD

### 🥈 #2: BTS On-Time Performance (FREE & DETAILED)

**What you get:**
- Individual flight records
- Actual departure/arrival times
- Flight numbers, tail numbers
- Delay information

**URL:**
https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ

### 🥉 #3: FlightAware (PAID BUT EXCELLENT)

**What you get:**
- Real-time tracking
- Historical flight paths
- Better small airport coverage
- API access

**URL:**
https://flightaware.com/live/airport/PAOT

## Project Scripts

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `get_bts_data.py` | Show instructions & open BTS site | Start here |
| `analyze_bts_data.py` | Process downloaded BTS data | After downloading CSV |
| `test_api.py` | Test OpenSky API access | Troubleshooting only |
| `test_api_comprehensive.py` | Comprehensive OpenSky tests | Research purposes |
| `collect_otz_flights.py` | Attempt OpenSky collection | Not recommended |

## Airport Codes

- **IATA:** OTZ
- **ICAO:** PAOT
- **FAA:** OTZ
- **Name:** Ralph Wien Memorial Airport
- **Location:** Kotzebue, Alaska

## Example: BTS Data Workflow

```bash
# 1. See instructions and open website
python get_bts_data.py

# 2. Download CSV from BTS (follow on-screen instructions)
#    Save to: data/your_downloaded_file.csv

# 3. Analyze the data
python analyze_bts_data.py

# Output will show:
# - Flights per year
# - Top airlines
# - Top origin airports
# - Passenger statistics
```

## Airlines Serving OTZ

1. **Alaska Airlines** - Primary carrier
   - ANC → OTZ (Anchorage to Kotzebue)
   - FAI → OTZ (Fairbanks to Kotzebue)

2. **Regional Carriers:**
   - Bering Air (https://beringair.com/)
   - Ravn Alaska (https://ravnalaska.com/)
   - Grant Aviation

## Questions?

**Q: Can I still try OpenSky?**  
A: Yes, but you'll need an account and may still hit limits. The scripts are included but not recommended.

**Q: How long does BTS data take to download?**  
A: 1-2 minutes to configure filters, instant download (small file).

**Q: Is BTS data really complete?**  
A: Yes, for all scheduled commercial carriers. It won't include:
- Private flights
- Charter flights (unless by scheduled carrier)
- Military flights
- General aviation

**Q: What if I need individual flight numbers?**  
A: Use BTS On-Time Performance data (Method #2 in get_bts_data.py)

## Support

This project provides tools for both approaches:
- ✅ BTS data (recommended): `get_bts_data.py` + `analyze_bts_data.py`
- ⚠️ OpenSky API (limited): `test_api.py` + `collect_otz_flights.py`
