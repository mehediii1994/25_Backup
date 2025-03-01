

"""
২। দুই অঙ্কের যেকোনো সংখ্যার অঙ্ক দুইটির স্থান পরিবর্তন কর। বড় সংখ্যাটি থেকে ছোট সংখ্যাটি বিয়োগ করে বিয়োগফলকে ৯ দ্বারা ভাগ দাও। ভাগশেষ হবে শূন্য।

এর মানে হলো:

১. যেকোনো দুটি অঙ্ক দিয়ে একটি সংখ্যা তৈরি করুন (যেমন: ২৩)।
২. অঙ্ক দুটি স্থান পরিবর্তন করে নতুন একটি সংখ্যা তৈরি করুন (যেমন: ৩২)।
৩. বড় সংখ্যাটি থেকে ছোট সংখ্যাটি বিয়োগ করুন (যেমন: ৩২ - ২৩ = ৯)।
৪. বিয়োগফলটিকে ৯ দিয়ে ভাগ করুন (যেমন: ৯ / ৯ = ১)।
৫. ভাগশেষ সবসময় শূন্য হবে।

"""

def check_two_digit_difference_property():
    """
    Dui ongker jekono songkhar ongko duitir sthan poriborton kore, boro songkhata theke choto songkhata biyog kore,
    biyogfolke 9 diye vag dile vagsesh shunno hobe kina ta porikkha kore.
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
    
    if num > reversed_num:
        difference = num - reversed_num
    else:
        difference = reversed_num - num
    
    quotient = difference // 9
    remainder = difference % 9
    
    print(f"Biyogfol: {difference}") # Biyogfol:
    print(f"{difference} / 9 = {quotient}, vagsesh = {remainder}") # vagsesh =
    
    if remainder == 0:
        print("Vagsesh shunno.") # Vagsesh shunno.
    else:
        print("Vagsesh shunno noy.") # Vagsesh shunno noy.

check_two_digit_difference_property()