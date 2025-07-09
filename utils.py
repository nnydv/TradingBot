# utils.py
def validate_input(symbol, side, order_type, quantity, price=None):
    # Validate symbol (e.g., BTCUSDT)
    if not symbol.isalpha() or len(symbol) < 3:
        raise ValueError("Invalid symbol. Example: BTCUSDT")
    
    # Validate side (BUY/SELL)
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be 'BUY' or 'SELL'")
    
    # Validate order type (MARKET/LIMIT)
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be 'MARKET' or 'LIMIT'")
    
    # Validate quantity (must be positive)
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
    except ValueError:
        raise ValueError("Quantity must be a number")
    
    # Validate price (if LIMIT order)
    if order_type == "LIMIT":
        if not price:
            raise ValueError("Price is required for LIMIT orders")
        try:
            price = float(price)
            if price <= 0:
                raise ValueError("Price must be positive")
        except ValueError:
            raise ValueError("Price must be a number")