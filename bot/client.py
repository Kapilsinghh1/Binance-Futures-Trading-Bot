#This files job is simply : Create a connection between our Python bot and Binance

#this code defines a function `get_client()` that creates and returns a Binance Futures Testnet client using the API key and secret stored in environment variables. It uses the `python-binance` library to interact with the Binance API and the `dotenv` library to load environment variables from a `.env` file. The client is configured to use the Futures Testnet URL.

from binance.client import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv() #means load the variables from the .env file

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def get_client(): 
    """
    Creates and returns a Binance Futures Testnet client
    """

    client = Client(API_KEY, API_SECRET) # Create a Binance connection object using the API key and secret from environment variables after this bot can send trading commands to Binance and receive data from it

    # Set Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client