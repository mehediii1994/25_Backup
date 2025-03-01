#সংখ্যাকে দুইটি স্বাভাবিক সংখ্যার বর্গের সমষ্টি রূপে প্রকাশ"

def find_squares_sum(number):
    """
    Finds two natural numbers whose squares sum up to the given number.

    Args:
        number: The number to be expressed as the sum of two squares.

    Returns:
        A tuple containing the two natural numbers (a, b) if found,
        or None if no such pair exists.
    """

    for a in range(1, int(number**0.5) + 1):
        b_squared = number - a**2
        b = int(b_squared**0.5)
        if b**2 == b_squared:
            return (a, b)
    return None

# Get input from the user
try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Please enter a non-negative number.")
    else:
        result = find_squares_sum(num)
        if result:
            print(f"{num} = {result[0]}² + {result[1]}²")
        else:
            print(f"{num} cannot be expressed as the sum of two squares.")
except ValueError:
    print("Invalid input. Please enter an integer.")