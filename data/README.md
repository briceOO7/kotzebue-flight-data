# Data Directory

This directory is for storing flight data files.

## Sample Data

`sample_bts_data.csv` - Example BTS T-100 data format showing how the downloaded data should look.

## Your Downloaded Data

Place your downloaded BTS CSV files here:
- From: https://www.transtats.bts.gov/Tables.asp?QO_VQ=EFD
- Files will be automatically detected by `analyze_bts_data.py`

## Processed Data

When you run `analyze_bts_data.py`, it will create:
- `otz_arrivals_processed_YYYYMMDD.csv` - Filtered and processed results

## Notes

- `.csv` files in this directory are gitignored (except sample_bts_data.csv)
- You can have multiple CSV files; the script will use the first one found
- Sample data is for demonstration only - download real data from BTS
