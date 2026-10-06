stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}
total_investment = 0
print("===== Stock Portfolio Tracker =====")
print("\nAvailable Stocks:")
for stock in stock_prices:
    print(stock, "- $", stock_prices[stock])
number = int(input("\nHow many stocks do you want to add? "))
portfolio = []
for i in range(number):
    stock_name = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment
        portfolio.append((stock_name, quantity, price, investment))
    else:
        print("Stock not available in the list.")
print("\n===== Your Portfolio =====")
for stock, quantity, price, investment in portfolio:
    print("Stock:", stock)
    print("Quantity:", quantity)
    print("Price: $", price)
    print("Investment: $", investment)
    print()
print("----------------------------")
print("Total Investment: $", total_investment)
print("----------------------------")
save = input("\nDo you want to save the result? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("===== Stock Portfolio =====\n\n")
        for stock, quantity, price, investment in portfolio:
            file.write("Stock: " + stock + "\n")
            file.write("Quantity: " + str(quantity) + "\n")
            file.write("Price: $" + str(price) + "\n")
            file.write("Investment: $" + str(investment) + "\n\n")
        file.write("----------------------------\n")
        file.write("Total Investment: $" + str(total_investment))
    print("Portfolio saved successfully in portfolio.txt")