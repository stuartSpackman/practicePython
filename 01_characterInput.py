"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that
they will turn 100 years old.

Note: for this exercise, the expectation is that you explicitly
write out the year (and therefore be out of date the next year).
"""
name = input('Enter your name: ')
age = int(input('Enter your age: '))
hundred = 2023 + 100 - age
print(name + ', you will turn 100 in the year ' + str(hundred) + '.')
