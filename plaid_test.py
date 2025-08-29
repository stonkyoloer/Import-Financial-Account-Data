# Step 1: Basic Plaid Connection Test
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_credentials():
    client_id = os.getenv('PLAID_CLIENT_ID')
    secret = os.getenv('PLAID_SECRET')
    
    if client_id and secret:
        print("✅ Credentials found!")
        print(f"Client ID: {client_id[:8]}...")  # Show first 8 chars only
        return True
    else:
        print("❌ Credentials missing!")
        print("Add PLAID_CLIENT_ID and PLAID_SECRET to .env file")
        return False

if __name__ == "__main__":
    print("🚀 Testing Plaid credentials...")
    test_credentials()
