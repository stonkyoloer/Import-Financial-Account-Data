# Step 3: Wells Fargo Account Connection (Fixed)
import os
from dotenv import load_dotenv
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.country_code import CountryCode
from plaid.model.products import Products
from plaid.configuration import Configuration
from plaid.api_client import ApiClient

load_dotenv()

class WellsFargoConnector:
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
        print("✅ Wells Fargo connector initialized")

    def get_link_token(self):
        """Get link token specifically for Wells Fargo"""
        try:
            request = LinkTokenCreateRequest(
                products=[Products('transactions')],  # Fixed: Only transactions
                client_name="Alexander's Wells Fargo Import",
                country_codes=[CountryCode('US')],
                language='en',
                user=LinkTokenCreateRequestUser(client_user_id='wells-fargo-user')
            )
            response = self.client.link_token_create(request)
            link_token = response['link_token']
            print(f"✅ Link token ready for Wells Fargo connection")
            print(f"🔗 Token: {link_token[:25]}...")
            return link_token
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

if __name__ == "__main__":
    print("🏦 Wells Fargo Connection Setup...")
    connector = WellsFargoConnector()
    token = connector.get_link_token()
    
    if token:
        print("\n📋 Next step: Use this token to connect Wells Fargo")
        print("💡 We'll build the connection interface next!")
