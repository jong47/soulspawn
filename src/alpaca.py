import os
# from dotenv import load_dotenv
from alpaca.broker import BrokerClient

BROKER_API_KEY = os.getenv("BROKER_API_KEY")
BROKER_SECRET_KEY = os.getenv("BROKER_SECRET_KEY")

broker_client = BrokerClient(
    api_key=BROKER_API_KEY,
    secret_key=BROKER_SECRET_KEY,
    sandbox=True,
)
