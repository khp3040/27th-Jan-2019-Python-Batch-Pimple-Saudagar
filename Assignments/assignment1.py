
# coding: utf-8

# In[3]:

#1. Write a Python program to print all natural numbers from 1 to n. 
n = input('Enter a number: ')
for i in range(1, n+1):
    print i,

#2. Write a Python program to print all natural numbers in reverse (from n to 1).
print '\n'
n = input('Enter a number: ')
for i in range(1, n+1)[::-1]:
    print i,
print '\n'
# for i in range(n, 1, -1):

#3. Write a Python program to print all alphabets from a to z.
for i in range(65, 65+26):
    print chr(i),

print '\n'
#4. Write a Python program to print all even numbers between 1 to 100. 
for i in range(2, 100, 2):
    print i,

print '\n'
#5. Write a Python program to print all odd number between 1 to 100.
for i in range(1, 100, 2):
    print i,
    
print '\n'


# In[ ]:



