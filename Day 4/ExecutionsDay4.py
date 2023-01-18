
# coding: utf-8

# In[34]:

for i in range(2, 100):
    for j in range(2, int(i/2)+1):
        if i % j == 0:
            break
    else:
        print '%d is a prime number' %(i)


# In[28]:

number = input('Enter a number: ')
for i in range(2, int(number/2)):
    if number % i == 0:
        break
else:
    print '%d is a prime number' %(number)


# In[ ]:

print [i for i in 'Python']
print [i ** 3 for i in range(10)]

# [i for i in iterable if condition]
print [i for i in 'Python' if i in 'thn']
print [i ** 3 for i in range(10) if i % 2]

for i in [['Python', 'Django'], ['Java', 'JSP']]:
    print "Priting : ", i
    for j in i:
        print "printing: ", j
        for z in j:
            print z
            
# [j for i in iterable for j in i]
print [j for i in [['Python', 'Django'], ['Java', 'JSP']] 
       for j in i]

print [j for i in [['Python', 'Django'], ['Java', 'JSP']] 
       for j in i if j in ['Python', 'Java']]

number = input('Enter a number: ')
if all([number % i for i in range(2, int(number/2))]):
    print '%d is a prime number' %(number)
else:
    print '%d is a not prime number' %(number)

