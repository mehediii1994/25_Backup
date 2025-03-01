
#উদাহরণ ১। সংখ্যাগুলোর পরবর্তী দুইটি সংখ্যা নির্ণয় কর: ৩, ১০, ১৭, ২৪, ৩১, ...

def find_next_numbers(numbers):
    """
    shongkhagular poroborti duiti shongkha nirnoy kore.

    Args:
        numbers: shongkhagular talika.

    Returns:
        poroborti duiti shongkhar talika.
    """

    if len(numbers) < 3:
        return "ontohto tinti shongkha din."

    difference = numbers[1] - numbers[0]

    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i-1] != difference:
            return "eti somantor dhara noy."

    next_number1 = numbers[-1] + difference
    next_number2 = next_number1 + difference

    return [next_number1, next_number2]

# shongkhagular input nin
numbers_input = input("shongkhagulo comma diye likhun: ")
numbers_list = [int(x) for x in numbers_input.split(',')]

# poroborti shongkhagulo nirnoy korun
next_numbers = find_next_numbers(numbers_list)

# folafol prodorshon korun
if isinstance(next_numbers, list):
    print("poroborti shongkhagulo:", next_numbers)
else:
    print(next_numbers)