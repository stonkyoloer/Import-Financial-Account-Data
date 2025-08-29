# Step 8: Save Wells Fargo Data to CSV Files
import os
import csv
import json
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from datetime import datetime, timedelta

load_dotenv()

class DataSaver:
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
        print("✅ Data saver initialized")

    def save_accounts_to_csv(self):
        """Save accounts to CSV file"""
        try:
            request = AccountsGetRequest(access_token=self.access_token)
            response = self.client.accounts_get(request)
            accounts = response['accounts']
            
            filename = f"wells_fargo_accounts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['account_id', 'name', 'type', 'subtype', 'current_balance', 'available_balance']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for account in accounts:
                    writer.writerow({
                        'account_id': account['account_id'],
                        'name': account['name'],
                        'type': account['type'],
                        'subtype': account['subtype'],
                        'current_balance': account['balances']['current'],
                        'available_balance': account['balances'].get('available', '')
                    })
            
            print(f"✅ Accounts saved to: {filename}")
            return filename
        except Exception as e:
            print(f"❌ Error saving accounts: {e}")
            return None

    def save_transactions_to_csv(self, days=90):
        """Save transactions to CSV file"""
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
            
            filename = f"wells_fargo_transactions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['transaction_id', 'account_id', 'date', 'name', 'amount', 'category', 'merchant_name']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for txn in transactions:
                    categories = txn.get('category', [])
                    category_str = ', '.join(categories) if categories else 'Uncategorized'
                    
                    writer.writerow({
                        'transaction_id': txn['transaction_id'],
                        'account_id': txn['account_id'],
                        'date': txn['date'],
                        'name': txn['name'],
                        'amount': txn['amount'],
                        'category': category_str,
                        'merchant_name': txn.get('merchant_name', '')
                    })
            
            print(f"✅ Transactions saved to: {filename}")
            return filename
        except Exception as e:
            print(f"❌ Error saving transactions: {e}")
            return None

if __name__ == "__main__":
    print("💾 Saving Wells Fargo Data to CSV...")
    
    # Use the same access token
    access_token = "access-sandbox-b64a857b-0332-4c0d-bcdd-0359387d0edb"
    
    saver = DataSaver(access_token)
    
    print("\n1️⃣ Saving accounts...")
    accounts_file = saver.save_accounts_to_csv()
    
    print("\n2️⃣ Saving transactions...")
    transactions_file = saver.save_transactions_to_csv()
    
    if accounts_file and transactions_file:
        print(f"\n🎉 Data export complete!")
        print(f"📊 Accounts: {accounts_file}")
        print(f"💳 Transactions: {transactions_file}")
