# Binance Futures Trading Bot (Testnet)

## Overview
This project is a simplified trading bot built in Python that interacts with the Binance Futures Testnet API.  
The bot allows users to place MARKET and LIMIT orders through a command-line interface.

## Features
- Place MARKET orders
- Place LIMIT orders
- Support BUY and SELL sides
- Input validation
- Logging of API requests and responses
- Error handling
- Clean project structure

## Project Structure

trading_bot
│                                          
├── bot
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── cli.py
│
├── logs
├── .env
├── requirements.txt
└── README.md

## Setup Instructions

### 1 Install dependencies
pip install -r requirements.txt


### 2 Create Binance Futures Testnet API Keys

Go to:
https://testnet.binancefuture.com

Generate API keys and store them in `.env`
API_KEY=your_api_key
API_SECRET=your_secret_key


### 3 Run MARKET Order
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

### 4 Run LIMIT Order
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 65000


## Logging
Logs are stored in: logs/trading_bot.log


The log file records:

- API requests
- order responses
- errors

## Example Output
Order Response

Order ID : 123456789
Symbol : BTCUSDT
Status : NEW
Order Type : MARKET
Side : BUY
Quantity : 0.01
Executed Qty : 0.00
Average Price : 0.00


## Author
Python Developer Intern Assignment
