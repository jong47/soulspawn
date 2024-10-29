import os
import pytest
from dotenv import load_dotenv
from alpaca.trading.client import TradingClient

@pytest.fixture(scope="module")
def trading_client():
    load_dotenv("keys.env")
    api_key = os.getenv("BROKER_API_KEY")
    api_secret = os.getenv("BROKER_SECRET_KEY")

    if not api_key or not api_secret:
        pytest.skip("Alpaca API credentials not available")
    
    return TradingClient(api_key, api_secret, paper=True)