

"""
১। দুই অঙ্কের যেকোনো সংখ্যা নাও। সংখ্যার অঙ্ক দুইটির স্থান বদল করে প্রাপ্ত নতুন সংখ্যাটির সাথে আগের সংখ্যাটি যোগ কর। যোগফল কে ১১ দ্বারা ভাগ কর। ভাগশেষ হবে শূন্য।   

এর মানে হলো:

১. যেকোনো দুটি অঙ্ক দিয়ে একটি সংখ্যা তৈরি করুন (যেমন: ২৩)।
২. অঙ্ক দুটি স্থান পরিবর্তন করে নতুন একটি সংখ্যা তৈরি করুন (যেমন: ৩২)।
৩. নতুন সংখ্যাটি এবং আগের সংখ্যাটি যোগ করুন (যেমন: ২৩ + ৩২ = ৫৫)।
৪. যোগফলটিকে ১১ দিয়ে ভাগ করুন (যেমন: ৫৫ / ১১ = ৫)।
৫. ভাগশেষ সবসময় শূন্য হবে।

"""

def check_two_digit_number_property():
    """
    Dui ongker jekono songkha niye, ongko duto sthan poriborton kore prapto notun songkhatair sathe
    ager songkhata jog kore, jogfolke 11 diye vag korle vagsesh shunno hobe kina ta porikkha kore.
    """
    
    while True:
        try:
            num = int(input("Dui ongker ekta songkha likhun (10 theke 99 er moddhe): ")) # Dui ongker ekta songkha likhun (10 theke 99 er moddhe)
            
            if 10 <= num <= 99:
                break
            else:
                print("Doya kore 10 theke 99 er moddhe ekta songkha likhun.") # Doya kore 10 theke 99 er moddhe ekta songkha likhun.
        except ValueError:
            print("Doya kore ekta songkha likhun.") # Doya kore ekta songkha likhun.
    
    first_digit = num // 10
    second_digit = num % 10
    
    reversed_num = second_digit * 10 + first_digit
    
    sum_of_numbers = num + reversed_num
    
    quotient = sum_of_numbers // 11
    remainder = sum_of_numbers % 11
    
    print(f"{num} + {reversed_num} = {sum_of_numbers}")
    print(f"{sum_of_numbers} / 11 = {quotient}, vagsesh = {remainder}") # vagsesh =
    
    if remainder == 0:
        print("Vagsesh shunno.") # Vagsesh shunno.
    else:
        print("Vagsesh shunno noy.") # Vagsesh shunno noy.

check_two_digit_number_property()