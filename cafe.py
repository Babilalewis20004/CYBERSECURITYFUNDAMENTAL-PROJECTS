# list containing menu items
menu = {'coffee',  'tea',  'sandwich',  'cake'}

# Dictionary containing item prices
price = {'coffee': 1.50, 'tea': 1.00, 'sandwich': 5.00, 'cake': 2.50}

# Dictionary containing stock count for each item
stock = {'coffee': 100, 'tea': 200, 'sandwich': 50, 'cake': 80}

# Calculate the total value of the stock
total_value = sum(stock[item] * price[item] for item in menu)

# Print out the total value of the stock
print("The total value of the stock is:", total_value)
