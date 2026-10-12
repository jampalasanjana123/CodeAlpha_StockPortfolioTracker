
# CodeAlpha Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

try:
    number = int(input("\nHow many stocks do you want to enter? "))

    if number <= 0:
        print("Please enter a positive number.")
    else:
        for i in range(number):
            stock = input(
                f"\nEnter stock name {i + 1}: "
            ).strip().upper()

            if stock not in stock_prices:
                print("Stock not available. Skipping.")
                continue

            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be positive. Skipping.")
                continue

            portfolio[stock] = (
                portfolio.get(stock, 0) + quantity
            )

        print("\n" + "=" * 40)
        print("         PORTFOLIO SUMMARY")
        print("=" * 40)

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            total_investment += investment

            print(
                f"{stock}: {quantity} shares x "
                f"${price} = ${investment}"
            )

        print("-" * 40)
        print(f"Total Investment: ${total_investment}")

        # Save the portfolio to a text file
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity

                file.write(
                    f"{stock}: Quantity={quantity}, "
                    f"Price=${price}, "
                    f"Investment=${investment}\n"
                )

            file.write(
                f"\nTotal Investment: ${total_investment}\n"
            )

        print("Portfolio saved to portfolio.txt")

except ValueError:
    print("Invalid input. Please enter numbers correctly.")
