# Step 2: Plaid API Connection (Fixed)
import os
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.country_code import CountryCode
from plaid.model.products import Products
from plaid.configuration import Configuration
from plaid.api_client import ApiClient

# Load environment variables
load_dotenv()

class PlaidConnection:
    def __init__(self):
        configuration = Configuration(
            host='https://sandbox.plaid.com',  # Fixed: direct URL
            api_key={
                'clientId': os.getenv('PLAID_CLIENT_ID'),
                'secret': os.getenv('PLAID_SECRET')
            }
        )
        api_client = ApiClient(configuration)
        self.client = plaid_api.PlaidApi(api_client)
        print("✅ Plaid client initialized")

    def create_link_token(self):
        """Create a link token for Plaid Link"""
        try:
            request = LinkTokenCreateRequest(
                products=[Products('transactions')],
                client_name="Alexander's Accounting SaaS",
                country_codes=[CountryCode('US')],
                language='en',
                user=LinkTokenCreateRequestUser(client_user_id='user-001')
            )
            response = self.client.link_token_create(request)
            print("✅ Link token created successfully!")
            return response['link_token']
        except Exception as e:
            print(f"❌ Error creating link token: {e}")
            return None

if __name__ == "__main__":
    print("🚀 Testing Plaid connection...")
    plaid = PlaidConnection()
    token = plaid.create_link_token()
    if token:
        print(f"🔗 Link token: {token[:20]}...")
