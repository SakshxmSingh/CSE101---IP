# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 01

#--------------ques01------------------

n = int(input())
list_tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
list_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
list_ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
if 0<n<100:
    if n<10:
        print(list_ones[n])
    elif 10<=n<20:
        print(list_teens[int(str(n)[1])])
    elif n>=20:
        print(list_tens[int(str(n)[0])], list_ones[int(str(n)[1])])