# প্রথম দশটি বিজোড় সংখ্যার যোগফল নির্ণয়"।

def sum_of_first_n_odd_numbers(n):
  """Calculates the sum of the first n odd numbers."""
  return n * n

# Take input from the user
try:
  n = int(input("Enter the value of n (number of odd numbers to sum): "))
  if n <= 0:
    print("Please enter a positive integer.")
  else:
    # Calculate the sum
    result = sum_of_first_n_odd_numbers(n)
    # Print the result
    print(f"The sum of the first {n} odd numbers is: {result}")

except ValueError:
  print("Invalid input. Please enter an integer.")