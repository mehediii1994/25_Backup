# Shotkara_Lav.py

# Function to calculate percentage profit
def calculate_percentage_profit(cost_price, selling_price):
    profit = selling_price - cost_price
    percentage_profit = (profit / cost_price) * 100
    return percentage_profit

# Input from user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Calculate and display the percentage profit
percentage_profit = calculate_percentage_profit(cost_price, selling_price)
print(f"The percentage profit is: {percentage_profit:.2f}%")