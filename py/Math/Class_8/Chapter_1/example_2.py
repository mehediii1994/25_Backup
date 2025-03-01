#উদাহরণ ২। সংখ্যাগুলোর পরবর্তী সংখ্যাটি নির্ণয় কর: ১, ৪, ৯, ১৬, ২৫, ...

def find_next_square(numbers):
    # শেষ সংখ্যার বর্গমূল নির্ণয়
    last_number = numbers[-1]
    next_number = (int(last_number ** 0.5) + 1) ** 2
    return next_number

# ইনপুট নেওয়া
input_numbers = input("songkhagulo comma diye likhun (jemon: 1, 4, 9, 16, 25): ")
numbers = list(map(int, input_numbers.split(',')))

# পরবর্তী সংখ্যা গণনা
next_number = find_next_square(numbers)
print(f"poroborti songkhata holo: {next_number}")