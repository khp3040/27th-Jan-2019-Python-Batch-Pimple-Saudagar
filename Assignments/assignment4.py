
# coding: utf-8

# In[8]:

#16. Write a Python program to enter a number and print its reverse.
n = str(input('Enter a number: '))
print int(n[::-1])

#17. Write a Python program to check whether a number is palindrome or not.
n = str(input('Enter a number: '))
print int(n[::-1]) == int(n)

#18. Write a Python program to find frequency of each digit in a given integer.
#18. Write a Python program to find frequency of each digit in a given integer.
number = 111221879 # Aggregration of data
count = dict() # Key is unique in a dict

for i in str(number):
    if i in count: # Check karo i is key in dict or not
        count[i] += 1
    else:
        count[i] = 1

for i in count:
    print '%d available %d times in number' %(int(i), count[i])

#19. Write a Python program to find power of a each number using for loop.
n = str(input('Enter a number: '))
for i in n:
    print int(i) ** 2,

print '\n'

#20. Write a Python program to print all ASCII character with their values.
for i in range(1, 128):
    print i, chr(i),
    print '\n'

