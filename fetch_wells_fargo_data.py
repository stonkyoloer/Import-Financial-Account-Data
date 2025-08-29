# Step 7: Fetch Wells Fargo Account Data and Transactions (Fixed)
import os
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from datetime import datetime, timedelta
import json

load_dotenv()

class WellsFargoDataFetcher:
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
        print("✅ Wells Fargo data fetcher ready")

    def fetch_all_accounts(self):
        """Get all Wells Fargo accounts"""
        try:
            request = AccountsGetRequest(access_token=self.access_token)
            response = self.client.accounts_get(request)
            accounts = response['accounts']
            
            print(f"\n🏦 Wells Fargo Accounts ({len(accounts)} found):")
            print("-" * 60)
            
            for account in accounts:
                name = account['name']
                account_type = account['type']
                subtype = account['subtype']
                balance = account['balances']['current']
                available = account['balances'].get('available', 'N/A')
                
                print(f"📋 Account: {name}")
                print(f"   Type: {account_type} ({subtype})")
                print(f"   Current Balance: ${balance}")
                print(f"   Available: ${available}")
                print()
            
            return accounts
        except Exception as e:
            print(f"❌ Error fetching accounts: {e}")
            return None

    def fetch_transactions(self, days=90):
        """Get recent Wells Fargo transactions"""
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
            
            print(f"\n💳 Wells Fargo Transactions (Last {days} days - {len(transactions)} found):")
            print("-" * 80)
            
            for i, txn in enumerate(transactions[:10], 1):  # Show first 10
                date = txn['date']
                name = txn['name']
                amount = txn['amount']
                # Fix category handling
                categories = txn.get('category', [])
                if categories:
                    category = ', '.join(categories)
                else:
                    category = 'Uncategorized'
                
                print(f"{i:2d}. {date} | {name[:30]:<30} | ${amount:>8.2f} | {category}")
            
            if len(transactions) > 10:
                print(f"    ... and {len(transactions) - 10} more transactions")
            
            return transactions
        except Exception as e:
            print(f"❌ Error fetching transactions: {e}")
            return None

if __name__ == "__main__":
    print("🚀 Fetching Wells Fargo Data...")
    
    # Use the access token from previous step
    access_token = "access-sandbox-b64a857b-0332-4c0d-bcdd-0359387d0edb"
    
    print(f"🔑 Using access token: {access_token[:25]}...")
    
    fetcher = WellsFargoDataFetcher(access_token)
    
    # Get accounts first
    accounts = fetcher.fetch_all_accounts()
    
    # Then get transactions
    if accounts:
        transactions = fetcher.fetch_transactions()
        
        if transactions:
            print(f"\n🎉 Success! Retrieved {len(accounts)} accounts and {len(transactions)} transactions")
