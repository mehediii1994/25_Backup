# Function to calculate percentage loss
def calculate_percentage_loss(cost_price, selling_price):
    if cost_price <= 0:
        return "Cost price should be greater than zero."
    loss = cost_price - selling_price
    percentage_loss = (loss / cost_price) * 100
    return percentage_loss

# Input from user
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Calculate and display the percentage loss
percentage_loss = calculate_percentage_loss(cost_price, selling_price)
print(f"The percentage loss is: {percentage_loss:.2f}%")