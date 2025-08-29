# Step 6: Test with Plaid's Built-in Sandbox Accounts
import os
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.products import Products
from plaid.configuration import Configuration
from plaid.api_client import ApiClient
from datetime import datetime, timedelta

load_dotenv()

class SandboxTester:
    def __init__(self):
        configuration = Configuration(
            host='https://sandbox.plaid.com',
            api_key={
                'clientId': os.getenv('PLAID_CLIENT_ID'),
                'secret': os.getenv('PLAID_SECRET')
            }
        )
        api_client = ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
        print("✅ Sandbox tester initialized")

    def create_sandbox_item(self):
        """Create a sandbox Wells Fargo account with test data"""
        try:
            # Create sandbox public token for Wells Fargo
            request = SandboxPublicTokenCreateRequest(
                institution_id='ins_4',  # Wells Fargo institution ID
                initial_products=[Products('transactions')]
            )
            response = self.client.sandbox_public_token_create(request)
            public_token = response['public_token']
            
            print("✅ Created sandbox Wells Fargo account")
            print(f"🔗 Public token: {public_token[:25]}...")
            
            # Exchange for access token
            exchange_request = ItemPublicTokenExchangeRequest(
                public_token=public_token
            )
            exchange_response = self.client.item_public_token_exchange(exchange_request)
            access_token = exchange_response['access_token']
            
            print("✅ Exchanged for access token")
            print(f"🔑 Access token: {access_token[:25]}...")
            
            return access_token
        except Exception as e:
            print(f"❌ Error creating sandbox item: {e}")
            return None

if __name__ == "__main__":
    print("🧪 Creating sandbox Wells Fargo account...")
    tester = SandboxTester()
    access_token = tester.create_sandbox_item()
    
    if access_token:
        print(f"\n💾 Save this access token: {access_token}")
        print("📋 Next: We'll use this to fetch real account data!")
