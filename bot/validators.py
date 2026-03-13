# This file contains validation functions for the trading bot. These functions check if the input parameters for trading commands are valid before executing them. For example, they check if the trading symbol is valid, if the side of the trade is either BUY or SELL, if the order type is either MARKET or LIMIT, and if the quantity is greater than 0. If any of these checks fail, a ValueError is raised with an appropriate message.
def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(qty):
    if qty <= 0:
        raise ValueError("Quantity must be greater than 0")