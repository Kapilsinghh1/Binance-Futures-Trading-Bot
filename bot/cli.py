# This file is the main entry point for the trading bot. It uses the argparse module to read command line arguments for trading parameters such as symbol, side, type, quantity, and price. It then validates these inputs using functions from the validators module and places either a market or limit order using functions from the orders module. The results of the order placement are printed to the console, and any errors encountered during the process are logged using the logging module. The logging configuration is set up using the setup_logging function from the logging_config module.
import argparse #argparse is a Python module that reads command line arguments. It allows us to specify what arguments our program requires, and it will automatically generate help messages and handle errors when the user provides invalid input. In this code, we use argparse to read the trading parameters (symbol, side, type, quantity, and price) from the command line when we run the bot. This way, we can easily specify different trading commands without changing the code.
import logging
from urllib import response

from .orders import place_market_order, place_limit_order
from .validators import validate_side, validate_order_type, validate_quantity
from .logging_config import setup_logging


def main():

    # start logging system
    setup_logging()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        # validate inputs
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.qty)

        print("Order Request")
        print(args)

        if args.type == "MARKET":

            response = place_market_order(
                args.symbol,
                args.side,
                args.qty
            )

        else:

            if args.price is None:
                raise ValueError("LIMIT order requires price")

            response = place_limit_order(
                args.symbol,
                args.side,
                args.qty,
                args.price
            )

        print("Order Response")
        print("\nOrder Response")
        print("----------------")

        print(f"Order ID       : {response.get('orderId')}")
        print(f"Symbol         : {response.get('symbol')}")
        print(f"Status         : {response.get('status')}")
        print(f"Order Type     : {response.get('type')}")
        print(f"Side           : {response.get('side')}")
        print(f"Quantity       : {response.get('origQty')}")
        print(f"Executed Qty   : {response.get('executedQty')}")
        print(f"Average Price  : {response.get('avgPrice')}")

        logging.info("Order executed successfully")

    except Exception as e:

        logging.error(f"Error: {e}")
        print("Error:", e)


if __name__ == "__main__":
    main()