"""
Ask the user for a number.
Depending on whether the number is even or odd,
print out an appropriate message to the user.

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers:
    one number to check (call it num)
    and one number to divide by (check).
    If check divides evenly into num, tell that to the user.
    If not, print a different appropriate message.
"""

num = int(input('Enter a number: '))
check = int(input('Enter another number: '))
if num % 4 == 0:
    print('Your first number is even and divisible by 4.')
elif num % 2 == 0:
    print('Your first number is even.')
elif num % 2 == 1:
    print('Your first number is odd.')
if num % check == 0:
    print('Your first number can be divided evenly by your second number.')
else:
    print('Your first number cannot be divided evenly by your second number.')

