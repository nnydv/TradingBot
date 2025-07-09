# ui.py
from bot import BasicBot
from config import API_KEY, API_SECRET
from utils import validate_input

def main():
    bot = BasicBot(API_KEY, API_SECRET)

    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    order_type = input("Order Type (MARKET/LIMIT): ").upper()
    quantity = input("Quantity: ")

    price = None
    if order_type == "LIMIT":
        price = input("Limit Price: ")

    try:
        validate_input(symbol, side, order_type, quantity, price)
        response = bot.place_order(symbol, side, order_type, float(quantity), float(price) if price else None)
        print("Order response:", response)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
