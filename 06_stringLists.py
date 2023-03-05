"""
Ask the user for a string and print out whether this string is
a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""
word = input('Enter a string: ')
isPalindrome = True
for i in range(len(word)):
    if word[i] != word[-1-i]:
        isPalindrome = False
print('It is ' + str(isPalindrome) + ' that ' + word + ' is a palindrome.')
