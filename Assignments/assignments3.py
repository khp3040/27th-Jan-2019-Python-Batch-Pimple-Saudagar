
# coding: utf-8

# In[2]:

#11. Write a Python program to find first and last digit of a number.
n = str(input('Enter a number: '))
print "Last Digit: ", n[-1]
print "First Digit: ", n[0]

#12. Write a Python program to find sum of first and last digit of a number.
print int(n[0] + n[-1])

#13. Write a Python program to swap first and last digits of a number.
print int(n[-1] + n[1:-1] + n[0])

#14. Write a Python program to calculate sum of digits of a number.
sum1 = 0
for i in n:
    sum1 += int(i)
print sum1

#15. Write a Python program to calculate product of digits of a number.
prod = 1
for i in n:
    prod *= int(i)
print prod


# In[ ]:




# In[ ]:



