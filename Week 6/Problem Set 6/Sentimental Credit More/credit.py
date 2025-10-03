import sys
from cs50 import get_int

# Prompt user
number = get_int("Number: ")
num_str = str(number)

beginning2 = int(num_str[:2])
beginning1 = int(num_str[:1])
length = len(num_str)

# Luhn checksum
sumdigits = 0
reverse_digits = num_str[::-1]

for i, d in enumerate(reverse_digits):
    n = int(d)
    if i % 2 == 1:   # every other digit
        n *= 2
        if n > 9:
            n = n // 10 + n % 10
    sumdigits += n

valid = (sumdigits % 10 == 0)

# Identify card
if valid:
    if length == 15 and (beginning2 == 34 or beginning2 == 37):
        print("AMEX")
    elif length == 16 and 51 <= beginning2 <= 55:
        print("MASTERCARD")
    elif (length == 13 or length == 16) and beginning1 == 4:
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
