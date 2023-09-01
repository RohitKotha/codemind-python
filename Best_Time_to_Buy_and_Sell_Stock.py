# Input the number of days and the stock prices
n = int(input())
prices = list(map(int, input().split()))

# Initialize variables to keep track of the minimum price and maximum profit
min_price = float('inf')
max_profit = 0

# Iterate through the stock prices
for price in prices:
    # Update the minimum price if necessary
    if price < min_price:
        min_price = price
    # Calculate the potential profit if selling at the current price
    profit = price - min_price
    # Update the maximum profit if necessary
    if profit > max_profit:
        max_profit = profit

# Print the maximum profit
print(max_profit)
