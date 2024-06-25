### Strong number is the number if the sum of factorials of the digits from the number is same to that number then number is STRONG number
# eg 145 = 1! + 4! 5!

import math

def is_strong_number(num):
    digits= str(num)

    factorial_sum=0
    for i in digits:
        factorial_sum+= math.factorial(int(i))

    return num==factorial_sum



number= int(input())
if is_strong_number(number):
    print(f"{number} is Strong number")
else:
    print(f"{number} is not strong number")