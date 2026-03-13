'''This file sets up logging for the trading bot. It creates a logs folder if it does not exist and configures logging to write to a file named trading_bot.log with a specific format that includes the timestamp, log level, and message.'''
#Logging means recording what the program is doing.
#Instead of only printing on screen, we save information into a file. like program started , program ended, errors, etc. This helps us understand what happened when we look at the logs later.

import logging 
import os

def setup_logging():
    
    # create logs folder if it does not exist
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/trading_bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )