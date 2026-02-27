# Note: GitHub Actions Setup

The `.github/workflows/python-tests.yml` file is included in the repository but cannot be pushed via the current GitHub CLI token due to workflow scope limitations.

## To Enable GitHub Actions

If you want to enable automated testing on GitHub:

1. **Option A: Manual Upload**
   - Go to https://github.com/briceOO7/kotzebue-flight-data
   - Navigate to `.github/workflows/`
   - Upload `python-tests.yml` manually through GitHub's web interface

2. **Option B: Update Token**
   - Run: `gh auth refresh -s workflow`
   - Then: `git push origin main`

## What the Workflow Does

The CI/CD workflow will:
- Test on Python 3.8, 3.9, 3.10, 3.11, and 3.12
- Install dependencies
- Run linting checks
- Test script imports
- Verify sample data analysis

## Current Status

✅ Repository created  
✅ Documentation added  
✅ License added  
⚠️ GitHub Actions workflow ready but not pushed (requires workflow scope)
