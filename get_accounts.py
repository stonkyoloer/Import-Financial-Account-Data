# Step 5: Get Wells Fargo Account Data
import os
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from datetime import datetime, timedelta

load_dotenv()

class AccountDataFetcher:
    def __init__(self, access_token):
        configuration = Configuration(
            host='https://sandbox.plaid.com',
            api_key={
                'clientId': os.getenv('PLAID_CLIENT_ID'),
                'secret': os.getenv('PLAID_SECRET')
            }
        )
        api_client = ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
        self.access_token = access_token
        print("✅ Account data fetcher ready")

    def get_accounts(self):
        """Fetch all account information"""
        try:
            request = AccountsGetRequest(access_token=self.access_token)
            response = self.client.accounts_get(request)
            accounts = response['accounts']
            
            print(f"✅ Found {len(accounts)} accounts:")
            for i, account in enumerate(accounts, 1):
                print(f"   {i}. {account['name']} - {account['subtype']} - ${account['balances']['current']}")
            
            return accounts
        except Exception as e:
            print(f"❌ Error fetching accounts: {e}")
            return None

    def get_recent_transactions(self, days=30):
        """Fetch recent transactions"""
        try:
            start_date = datetime.now() - timedelta(days=days)
            end_date = datetime.now()
            
            request = TransactionsGetRequest(
                access_token=self.access_token,
                start_date=start_date.date(),
                end_date=end_date.date()
            )
            response = self.client.transactions_get(request)
            transactions = response['transactions']
            
            print(f"✅ Found {len(transactions)} transactions in last {days} days:")
            for i, txn in enumerate(transactions[:5], 1):  # Show first 5
                print(f"   {i}. {txn['date']} - {txn['name']} - ${txn['amount']}")
            
            if len(transactions) > 5:
                print(f"   ... and {len(transactions) - 5} more")
                
            return transactions
        except Exception as e:
            print(f"❌ Error fetching transactions: {e}")
            return None

if __name__ == "__main__":
    print("🏦 Testing with sandbox Wells Fargo data...")
    
    # We'll use a test access token for sandbox
    # In real app, this comes from the Link flow
    test_access_token = "access-sandbox-test-token"
    
    fetcher = AccountDataFetcher(test_access_token)
    
    print("\n1️⃣ Getting account information...")
    accounts = fetcher.get_accounts()
    
    if accounts:
        print("\n2️⃣ Getting recent transactions...")
        transactions = fetcher.get_recent_transactions()
