# Step 4: Simulate Wells Fargo Account Connection
import os
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.configuration import Configuration
from plaid.api_client import ApiClient

load_dotenv()

class BankAccountSimulator:
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
        print("✅ Bank simulator initialized")

    def exchange_public_token(self, public_token):
        """Exchange public token for access token"""
        try:
            request = ItemPublicTokenExchangeRequest(
                public_token=public_token
            )
            response = self.client.item_public_token_exchange(request)
            access_token = response['access_token']
            item_id = response['item_id']
            
            print("✅ Successfully exchanged tokens!")
            print(f"🔑 Access Token: {access_token[:20]}...")
            print(f"🏷️  Item ID: {item_id}")
            return access_token, item_id
        except Exception as e:
            print(f"❌ Token exchange error: {e}")
            return None, None

if __name__ == "__main__":
    print("🏦 Simulating Wells Fargo Connection...")
    simulator = BankAccountSimulator()
    
    # For sandbox testing, use this test public token
    test_public_token = "public-sandbox-b0e2c4ee-a763-4df5-bfe9-46a46bce993d"
    
    print(f"🧪 Using sandbox test token: {test_public_token[:20]}...")
    access_token, item_id = simulator.exchange_public_token(test_public_token)
    
    if access_token:
        print("\n🎉 Wells Fargo connection simulation successful!")
        print("📝 We now have access to account data")
