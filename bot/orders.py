# This file contains functions to place market and limit orders using the Binance API. It imports the Binance client from the `client` module and uses it to create orders. The `place_market_order` function places a market order with the specified symbol, side, and quantity,
# while the `place_limit_order` function places a limit order with the specified symbol, side, quantity, price, and time in force. Both functions log the details of the placed order using the logging module.
import logging
from .client import get_client # Import the function to get a Binance client instance.

client = get_client() # Create a Binance client instance to interact with the Binance API for placing orders.


def place_market_order(symbol, side, quantity):
    """
    Places a MARKET order
    """
    # The `place_market_order` function takes three parameters: `symbol`, which is the trading pair (e.g., "BTCUSDT"), `side`, which indicates whether the order is a buy or sell, and `quantity`, which specifies the amount of the asset to trade. It uses the Binance client to create a market order with these parameters and logs the details of the placed order.
    order = client.futures_create_order(               #this function futures_create_order is from the Binance API and it sends a request to binance API like a POST request with data or parameters to specify the details of the order, such as the trading symbol = BTCCUSDT , side (buy or sell), order type (market or limit), quantity, price, and time in force. Binance processes it and sends a response. and the response is stored in order variable. The order variable contains details about the placed order, such as the order ID, status, and other relevant information.
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logging.info(f"Market order placed: {order}") # This line logs the details of the placed market order using the logging module. and it will be saved in the trading_bot.log file with a timestamp, log level, and message that includes the details of the order. This helps us keep track of the orders placed by the bot and can be useful for debugging and monitoring purposes. it automatically saves the log in log folder with filename trading_bot.log because we set it up in logging_config.py file.

    return order # The function returns the API response from the function call, which contains the details of the placed market order, which can be used for further processing or tracking.


def place_limit_order(symbol, side, quantity, price):
    """
    Places a LIMIT order
    """

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    logging.info(f"Limit order placed: {order}")

    return order