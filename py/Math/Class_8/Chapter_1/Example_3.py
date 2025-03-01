
#উদাহরণ ৩। সংখ্যাগুলোর পরবর্তী সংখ্যাটি নির্ণয় কর: ১, ৫, ৬, ১১, ১৭, ২৮, ...

def find_next_number(numbers):
    """
    Given shongkhagular poroborti shongkha ber kore.

    Args:
        numbers: shongkhagular ekta list.

    Returns:
        poroborti shongkha, jodi sequence valid na hoy tahole None.
    """

    if len(numbers) < 3:
        return None  # Sequence pattern bujhar jonno kom shongkha.

    differences = []
    for i in range(1, len(numbers)):
        differences.append(numbers[i] - numbers[i - 1])

    if len(differences) < 2:
        return None

    next_difference = differences[-1] + differences[-2]
    next_number = numbers[-1] + next_difference

    return next_number

# User theke input neyar example
numbers_input = input("comma diye alada kore shongkhagulo enter korun: ")
numbers_list = [int(x) for x in numbers_input.split(',')]

next_num_user = find_next_number(numbers_list)

if next_num_user is not None:
    print("poroborti shongkha holo:", next_num_user)
else:
    print("poroborti shongkha ber kora possible na.")