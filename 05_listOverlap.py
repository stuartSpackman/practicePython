"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the
elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

    1. Randomly generate two lists to test this
    2. Write this in one line of Python
    (don’t worry if you can’t figure this out at this point -
    we’ll get to it soon)
"""
import random
a,b = [],[]
for i in range(1, random.randint(1,33)):
    a += [random.randint(1,99)]
for i in range(1, random.randint(1,33)):
    b += [random.randint(1,99)]
print('Here is one list: \n' + str(a))
print('Here is another list: \n' + str(b))
print('Here is their overlap: \n' + str([i for i in a if i in b]))
