
# coding: utf-8

# In[119]:

name = raw_input('Enter a name: ')
pay = int(raw_input('How much you need to pay? '))

print "Thanks", name, "for donation of", pay, "$ !"
print "Thanks %s for donation of %d$ !" %(name, pay) # Directives here


# In[62]:




# In[ ]:

a = 20L
print type(a)

# What are operators?
# Airthmetic Operators:  +, -, *, /, %, **, //
print 10 + 3
print 10 - 3
print 10 * 3
print 10 / 3.0
print 2 ** 2
print 10 % 2
print 10.0 // 3 # Floor Division
print 10 * 2 / 3 #??
print 10 * 2 ** 2 / 3 + 20 ** 2

# Bitwise
decimal = 10
print bin(decimal)
print oct(decimal)
print hex(decimal)

binary = '1010'
print int(binary, 2) # Decimal
print int(binary, 8) # Octal
print int(binary, 16) # Hexadecimal
# Python2 - int, float, long and complex
# Python3 - int, float, complex

print 10 << 3
print 20 >> 2
print 10 & 15
print 10 | 15
print 10 ^ 15

# Comparison opr
# >, <, >=, <=, ==, !=, <> (Not opr, which is not available in Python3)
print int(10.1) == 10 #True, False

print 10 <> 20

# Airthmetic, Bitwise, comparison
# Assignment Opr - +=, -=, *=, /=, **=
a = 10
a += 20 # a = a + 20
a += 1
print a

# is, is not

a = 10
b = a # b is poiting to memory location which has an access to a

c = 1000
d = 1000

print c is d # False
print c == d # True??

c = d
print c is d
print c == d

a = 255
b = 255

print a is b #?? 
a = 1 or 20
print a

name = 'Jatin'

location = "Pune"

statement = '''Jatin is taking class in Pune
at Pimple Saudagar Location
'''

print name, location
statement

# Raw string - which supress special string literals
print r"C:\Python\users\test\file.txt" # we have string literals

print u'This is unicode string'

# Only two airthmetic operator are overloaded in string class
# +, *

a = 10
print 'Jatin' + str(a)
print 'Jatin' * 'Miglani' # Error
print 'Jatin' + ' Miglani' # Applying an opr between two strings
print '**' * 20, '\nWelcome to Python class\n', '**' * 20

# Comparison opr
print ord('J'), ord('j')
print len('Jatin Miglani')
print 'jatin' > 'jat' # True or False??

name = 'Jatin' # +=, *=
name += ' Miglani'
name *= 2
print name

name = 'Jatin'
lastname = 'Jatin'

print id(name)
print id(lastname)

print name is lastname

help('if')
help(sum)

#membership opr in, not in

print 'x' not in 'Jatin'
print 'a' in 'Jatin'
print 'at' in 'Jatin'

string = 'This is my string'
string[0] = 't' # I am replacing T by t

name = 'madam'
print name == name[::-1]

