from binance.client import Client
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logging.basicConfig(filename='bot.log', level=logging.INFO)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }
            if order_type == Client.ORDER_TYPE_LIMIT:
                params["price"] = price
                params["timeInForce"] = Client.TIME_IN_FORCE_GTC

            response = self.client.futures_create_order(**params)
            logging.info(f"Order placed: {response}")
            return response
        except Exception as e:
            logging.error(f"Error placing order: {e}")
            return None

    def place_stop_limit(self, symbol, side, quantity, price, stop_price):
        try:
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                stopPrice=stop_price,
                closePosition=False,
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            logging.info(f"Stop-Limit Order placed: {response}")
            return response
        except Exception as e:
            logging.error(f"Error placing stop-limit order: {e}")
            return None
