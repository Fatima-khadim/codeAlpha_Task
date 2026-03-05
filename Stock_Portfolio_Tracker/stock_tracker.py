
stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2800}

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available. Choose from:", ", ".join(stock_prices.keys()))
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_investment = sum(stock_prices[s] * q for s, q in portfolio.items())

print("\nYour Portfolio:")
for s, q in portfolio.items():
    print(f"{s}: {q} shares × ${stock_prices[s]} = ${stock_prices[s] * q}")

print(f"Total Investment: ${total_investment}")