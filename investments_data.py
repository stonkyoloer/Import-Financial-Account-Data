#!/usr/bin/env python3
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class InvestmentDataCollector:
    def __init__(self):
        self.client_id = os.getenv('PLAID_CLIENT_ID')
        self.secret = os.getenv('PLAID_SECRET')
        self.base_url = 'https://sandbox.plaid.com'
        
        try:
            with open('access_token.txt', 'r') as f:
                self.access_token = f.read().strip()
        except:
            self.access_token = None
    
    def get_investment_holdings(self):
        if not self.access_token:
            return None
            
        url = f"{self.base_url}/investments/holdings/get"
        data = {
            'client_id': self.client_id,
            'secret': self.secret,
            'access_token': self.access_token
        }
        
        try:
            response = requests.post(url, json=data)
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None

def main():
    print("Starting investment analysis...")
    collector = InvestmentDataCollector()
    
    if not collector.access_token:
        print("No access token found")
        return
        
    print(f"Using token: {collector.access_token[:25]}...")
    holdings = collector.get_investment_holdings()
    
    if holdings:
        print(f"Holdings data: {len(holdings.get('holdings', []))} items")
    else:
        print("No holdings data")

if __name__ == "__main__":
    main()
