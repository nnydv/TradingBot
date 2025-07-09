from binance.client import Client
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logging.basicConfig(filename='bot.log', level=logging.INFO)

    def place_order(self, symbol, side, order_type, quantity, price=None):
    # Simulate a successful Binance response
        mock_response = {
            "symbol": symbol,
            "orderId": 123456,
            "status": "FILLED",
            "executedQty": str(quantity),
            "side": side,
            "type": order_type
        }
        print(f"DEBUG - Simulated Order: {mock_response}")
        logging.info(f"Order placed (simulated): {mock_response}")
        return mock_response

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
