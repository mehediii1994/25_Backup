"""""
# একটি দ্রব্য ২০ টাকা কিনে ৩০ টাকা বিক্রি করলে শতকরা কত পার্সেন্ট লাভ হবে ?

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

"""


"""""

#একটি দ্রব্য ৩৮০ টাকা বিক্রি করায় ২০ টাকা ক্ষতি হলো। শতকরা কত পার্সেন্ট ক্ষতি হলো ?

# Example calculation
example_selling_price = float(input("Enter the selling price: "))
khoti = float(input("Enter the loss: "))
example_cost_price = example_selling_price + khoti
example_percentage_loss = ((khoti / example_cost_price) * 100)
print(f"Example: The percentage loss is: {example_percentage_loss:.2f}%")
"""

"""
#টাকায় ৪টি কিনে ৫টি বিক্রি করলে কত পার্সেন্ট লাভ হবে ?

# Example calculation

kory_kra_holo =float(input("Enter the kory mora holo : "))
bikroy_kra_holo = float(input("Enter the bikroy kra holo : "))
love = kory_kra_holo-bikroy_kra_holo
example_percentage_loss = ((love / bikroy_kra_holo) * 100)
print(f"Example: The percentage loss is: {example_percentage_loss:.2f}%")

"""

"""
#টাকায় ৪টি কিনে ৫টি বিক্রি করলে কত পার্সেন্ট ক্ষতি  হবে ?
# Example calculation

kory_kra_holo =float(input("Enter the kory mora holo : "))
bikroy_kra_holo = float(input("Enter the bikroy kra holo : "))
khoti = kory_kra_holo-bikroy_kra_holo
example_percentage_loss = ((khoti / bikroy_kra_holo) * 100)
print(f"Example: The percentage loss is: {example_percentage_loss:.2f}%")

"""

#একটি হাঁস ২৭৫ টাকায় বিক্রি করলে ১৫ পার্সেন্ট  লাভ হয়। হাঁস টির ক্রয়মূল্য কত ?

bikroy_kra_holo = float(input("Enter the bikroy kra holo : "))
shotkora = float(input("Enter the shotkora Lave hoy : "))
probortito_mullo =100 +shotkora
kory_mullo = (bikroy_kra_holo * (100/probortito_mullo))
print(f"Koroy mullo holo: {kory_mullo:.2f}  taka")



