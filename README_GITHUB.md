# Kotzebue Flight Data Collector

![Kotzebue Airport](https://img.shields.io/badge/Airport-PAOT%20%2F%20OTZ-blue)
![Location](https://img.shields.io/badge/Location-Alaska%20%7C%20Arctic%20Circle-lightblue)
![Data Range](https://img.shields.io/badge/Data-2019--2025-green)

## 📊 Overview

A comprehensive data collection and analysis toolkit for commercial flights to/from Ralph Wien Memorial Airport (PAOT/OTZ) in Kotzebue, Alaska. This remote Arctic Circle airport serves as a critical transportation hub for Northwest Alaska.

### Features

✅ **BTS Data Analysis** - Process official US government flight statistics  
✅ **OpenSky Integration** - Alternative data source with API client  
✅ **Sample Data** - Ready-to-use example dataset  
✅ **Complete Documentation** - Multiple levels of guides  
✅ **Automated Analysis** - Generate statistics and reports  

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/briceOO7/kotzebue-flight-data.git
cd kotzebue-flight-data

# Install dependencies
pip install -r requirements.txt

# Try with sample data
python analyze_bts_data.py

# Get instructions for real data
python get_bts_data.py
```

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[README.md](README.md)** - Full documentation
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Project overview and findings
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines

## 🎯 What You'll Get

### Flight Statistics
- ✈️ Total flights by year
- 🏢 Breakdown by airline
- 🗺️ Origin airport analysis
- 👥 Passenger counts
- 📦 Freight and mail data

### Sample Output
```
Flights by Year:
  2019: 211 flights
  2020: 168 flights
  2021: 173 flights

Top Airlines:
  AS (Alaska Airlines): 518 flights
  8V (Bering Air): 34 flights

Top Origin Airports:
  ANC (Anchorage): 345 flights
  FAI (Fairbanks): 173 flights
```

## 📁 Project Structure

```
kotzebue-flight-data/
├── 📘 Documentation
│   ├── README.md
│   ├── QUICKSTART.md
│   ├── PROJECT_SUMMARY.md
│   └── CONTRIBUTING.md
│
├── 🐍 Python Scripts
│   ├── get_bts_data.py          # Step 1: Download instructions
│   ├── analyze_bts_data.py      # Step 2: Analyze data
│   ├── collect_otz_flights.py   # Alternative: OpenSky
│   └── test_api*.py             # API testing tools
│
├── 📊 Data
│   ├── sample_bts_data.csv      # Example dataset
│   └── README.md
│
└── ⚙️ Configuration
    ├── requirements.txt
    ├── LICENSE
    └── .github/workflows/
```

## 🌐 Data Sources

### Primary: Bureau of Transportation Statistics (BTS)
- **Free** and comprehensive
- 100% complete for commercial carriers
- Official US government data
- [Download here](https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD)

### Alternative: OpenSky Network
- Real-time flight tracking
- ADS-B based data
- Free API with limitations
- [OpenSky Network](https://opensky-network.org/)

## 🛫 About Kotzebue Airport

**Ralph Wien Memorial Airport (PAOT/OTZ)**
- Located in Kotzebue, Alaska
- 33 miles north of Arctic Circle
- Hub for Northwest Alaska
- Serves ~4,000 residents
- Critical for rural Alaska connectivity

### Airlines Serving OTZ
- 🛫 Alaska Airlines (primary carrier)
- 🛫 Bering Air
- 🛫 Ravn Alaska
- 🛫 Grant Aviation

## 💻 Usage Examples

### Analyze Your Downloaded Data
```python
from analyze_bts_data import load_bts_t100_data, analyze_otz_flights

# Load your data
df = load_bts_t100_data('data/your_file.csv')

# Analyze
analyze_otz_flights(df)
```

### Test OpenSky API
```bash
export OPENSKY_USERNAME="your_username"
export OPENSKY_PASSWORD="your_password"
python test_api_comprehensive.py
```

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution
- 📊 Additional data visualizations
- 🔧 More data source integrations
- 📝 Documentation improvements
- 🐛 Bug fixes and enhancements
- ✨ New features

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [OpenSky Network](https://opensky-network.org/) - Flight tracking data
- [Bureau of Transportation Statistics](https://www.transtats.bts.gov/) - Aviation statistics
- Airlines serving Kotzebue: Alaska Airlines, Bering Air, Ravn Alaska, Grant Aviation
- Alaska Department of Transportation & Public Facilities

## 📧 Contact

Found a bug? Have a question? [Open an issue](https://github.com/briceOO7/kotzebue-flight-data/issues)!

---

**⭐ If you find this project useful, please star it on GitHub!**

Made with ❤️ for Alaska aviation data analysis
