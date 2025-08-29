# Import Financial Account Data Using PLAID

1. A Python tool for importing and managing financial data using the PLAID API. 

2. This project provides a step-by-step workflow for connecting to financial accounts, fetching transaction data, and saving it for analysis.

## 📋 Prerequisites

- Python 3.7+
- Financial account(s)
- PLAID developer account (sandbox or development environment)
- Required Python packages (see requirements below)

## 🚀 Installation

**1. Clone this repository:**
```bash
git clone https://github.com/stonkyoloer/Import-Financial-Account-Data.git
cd Import-Financial-Account-Data
```

**2. Create a virtual environment:**
```bash
python -m venv plaid-env
source plaid-env/bin/activate  # On Windows: plaid-env\Scripts\activate
```

**3. Install required packages:**
```bash
pip install plaid-python requests pandas python-dotenv
```

## 📁 Project Structure

```
Import-Financial-Account-Data/
├── plaid_connect.py          # Step 1: Initial PLAID connection setup
├── get_accounts.py           # Step 2: Retrieve account information
├── plaid_test.py            # Step 3: Test API connection
├── sandbox_test.py          # Step 4: Sandbox environment testing
├── simulate_bank_connect.py # Step 5: Simulate bank connection flow
├── wells_fargo_connect.py   # Step 6: Wells Fargo specific connection
├── fetch_wells_fargo_data.py # Step 7: Fetch transaction data
├── save_data.py             # Step 8: Save data to files
├── wells_fargo_accounts_*.json # Generated account data
├── wells_fargo_transactions_*.json # Generated transaction data
└── .gitignore               # Git ignore file
```

## 📚 Step-by-Step Usage Guide

### Step 1: Initial PLAID Connection Setup
```bash
python plaid_connect.py
```
**Purpose:** Establishes the basic connection to PLAID API and validates credentials.
- Sets up PLAID client configuration
- Tests API connectivity
- Validates your PLAID credentials

### Step 2: Retrieve Account Information
```bash
python get_accounts.py
```
**Purpose:** Fetches and displays your connected account details.
- Retrieves account names, types, and balances
- Generates account mapping for transaction queries
- Saves account information to JSON files

### Step 3: Test API Connection
```bash
python plaid_test.py
```
**Purpose:** Comprehensive API testing and validation.
- Verifies all API endpoints are working
- Tests different request types
- Validates data formatting

### Step 4: Sandbox Environment Testing
```bash
python sandbox_test.py
```
**Purpose:** Tests the integration using PLAID's sandbox environment.
- Uses test credentials for safe testing
- Validates workflow without real bank data
- Perfect for development and testing

### Step 5: Simulate Bank Connection Flow
```bash
python simulate_bank_connect.py
```
**Purpose:** Simulates the complete bank connection process.
- Mimics the Link flow for connecting accounts
- Tests authentication workflows
- Prepares for real bank connection

### Step 6: Wells Fargo Specific Connection
```bash
python wells_fargo_connect.py
```
**Purpose:** Establishes connection specifically to Wells Fargo accounts.
- Handles Wells Fargo-specific authentication
- Sets up institution-specific parameters
- Creates secure connection tokens

### Step 7: Fetch Wells Fargo Transaction Data
```bash
python fetch_wells_fargo_data.py
```
**Purpose:** Downloads your actual Wells Fargo transaction history.
- Retrieves transactions for specified date ranges
- Handles pagination for large datasets
- Formats data for analysis
- **Output:** `wells_fargo_transactions_YYYYMMDD_HHMMSS.json`

### Step 8: Save Data to Files
```bash
python save_data.py
```
**Purpose:** Processes and saves the fetched data in various formats.
- Converts JSON to CSV for Excel compatibility
- Organizes data by categories
- Creates summary reports
- **Output:** Organized data files ready for analysis

## 📊 Generated Files

After running the complete workflow, you'll have:

- `wells_fargo_accounts_[timestamp].json` - Account information and balances
- `wells_fargo_transactions_[timestamp].json` - Complete transaction history
- `transaction_summary.csv` - Formatted transaction data for spreadsheets
- `account_balances.json` - Current account balances

## 🔧 Configuration

Create a `.env` file in your project root with your PLAID credentials:
```env
PLAID_CLIENT_ID=your_client_id_here
PLAID_SECRET=your_secret_here
PLAID_ENV=sandbox  # or 'development' or 'production'
```

## 📈 Next Steps

Once you have your data imported:
1. Analyze spending patterns
2. Create budget reports
3. Build financial dashboards
4. Set up automated data updates


---
