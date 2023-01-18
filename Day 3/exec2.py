Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> numbers = [1,2,3,4,5,6]
>>> 1 in numbers # membership opr
True
>>> employee1 = ['Jatin', 20000]
>>> employee2 = ['Rahul', 30000]
>>> employees = [employee1, employee2]
>>> len(employees)
2
>>> employees
[['Jatin', 20000], ['Rahul', 30000]]
>>> employees[0]
['Jatin', 20000]
>>> employees[1]
['Rahul', 30000]
>>> employees[0][0]
'Jatin'
>>> employees[1][0]
'Rahul'
>>> employees = [['Jatin', 'IT', ['Pune', 'Bangalore']], ['Rahul', 'HR', ['Delhi','Pune']]]
>>> employees[0]
['Jatin', 'IT', ['Pune', 'Bangalore']]
>>> employees[0][2]
['Pune', 'Bangalore']
>>> employees[0][2][0]
'Pune'
>>> len(employees[1][2])
2
>>> employees[1][2][0] = 'Kolkata'
>>> employees
[['Jatin', 'IT', ['Pune', 'Bangalore']], ['Rahul', 'HR', ['Kolkata', 'Pune']]]
>>> 
>>> numbers = [0,1,2,3]
>>> range(0, 10, 1)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 100, 2)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> range(2, 100, 2)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>> 
>>> table =
SyntaxError: invalid syntax
>>> table = 5
>>> range(table, table*10 + 1, table) # range(5, 51, 5)
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>>> help(range)
Help on built-in function range in module __builtin__:

range(...)
    range(stop) -> list of integers
    range(start, stop[, step]) -> list of integers
    
    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

>>> help(xrange)
Help on class xrange in module __builtin__:

class xrange(object)
 |  xrange(stop) -> xrange object
 |  xrange(start, stop[, step]) -> xrange object
 |  
 |  Like range(), but instead of returning a list, returns an object that
 |  generates the numbers in the range on demand.  For looping, this is 
 |  slightly faster than range() and more memory efficient.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __reduce__(...)
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __reversed__(...)
 |      Returns a reverse iterator.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> range(100, 1, -1)
[100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> 
>>> employee1 = {'name':'Jatin', 'age':35, 'salary':20000}
>>> employee2 = {'name':'Rahul', 'age':28, 'salary':10000}
>>> 
>>> print employee1
{'salary': 20000, 'age': 35, 'name': 'Jatin'}
>>> print employee2
{'salary': 10000, 'age': 28, 'name': 'Rahul'}
>>> 
>>> employee1['age']
35
>>> employee2['name']
'Rahul'
>>> employee1 = {'name':'Jatin', 'age':35, 'salary':20000, 'age':40}
>>> print employee1
{'salary': 20000, 'age': 40, 'name': 'Jatin'}
>>> employee1['salary']
20000
>>> employee1['salary'] = 30000
>>> employee1
{'salary': 30000, 'age': 40, 'name': 'Jatin'}
>>> employee1['city'] = 'Pune' # I am adding a new item
>>> employee1
{'salary': 30000, 'city': 'Pune', 'age': 40, 'name': 'Jatin'}
>>> 
>>> employee1 = {['name', 'name1']:'Jatin', 'age':35, 'salary':20000, 'age':40}

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    employee1 = {['name', 'name1']:'Jatin', 'age':35, 'salary':20000, 'age':40}
TypeError: unhashable type: 'list'
>>> employee1 = {'name':['Jatin', 'Rahul'], 'age':35, 'salary':20000, 'age':40}
>>> employee1['name']
['Jatin', 'Rahul']
>>> employee1['name'][0]
'Jatin'
>>> 
>>> employee1
{'salary': 20000, 'age': 40, 'name': ['Jatin', 'Rahul']}
>>> employee2 = employee1
>>> employee1['city'] = 'Bangalore'
>>> employee1
{'salary': 20000, 'city': 'Bangalore', 'age': 40, 'name': ['Jatin', 'Rahul']}
>>> employee2
{'salary': 20000, 'city': 'Bangalore', 'age': 40, 'name': ['Jatin', 'Rahul']}
>>> 
>>> del employee1['age']
>>> employee1
{'salary': 20000, 'city': 'Bangalore', 'name': ['Jatin', 'Rahul']}
>>> employee2
{'salary': 20000, 'city': 'Bangalore', 'name': ['Jatin', 'Rahul']}
>>> 
>>> 'city' in employee1 # membership with key only
True
>>> 'Bangalore' in employee1
False
>>> 
>>> employee1
{'salary': 20000, 'city': 'Bangalore', 'name': ['Jatin', 'Rahul']}
>>> list(employee1)
['salary', 'city', 'name']
>>> dict(one=1, two=2, three=3)
{'three': 3, 'two': 2, 'one': 1}
>>> 
>>> 
>>> name = 'Rahul'
>>> name2 = name
>>> 
>>> name2 += ' Gandhi'
>>> name2
'Rahul Gandhi'
>>> name #??
'Rahul'
>>> name is name2 #?
False
>>> 
>>> names = ['Rahul']
>>> names2 = names
>>> 
>>> names += ['Gandhi']
>>> names
['Rahul', 'Gandhi']
>>> names2 #??
['Rahul', 'Gandhi']
>>> 
>>> employees = [['Jatin', 35], ['Rahul', 25]]
>>> # listofList
>>> # lol
>>> 
>>> employees = [{'name':'Jatin', 'age':35}, {'name':'Rahul', 'age':25}]
>>> #listofDict
>>> employees[0]
{'age': 35, 'name': 'Jatin'}
>>> employees[0][0]

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    employees[0][0]
KeyError: 0
>>> employees[0]['age']
35
>>> employees[1]['name']
'Rahul'
>>> 
>>> employees = {1:['Jatin', 35], 2:['Rahul', 25]}
>>> employees = {1:{'name':'Jatin', 'age':35}, 2:{'name':'Rahul', 'age':25}}
>>> employees = {{'name':'Jatin', 'age':35}, {'name':'Rahul', 'age':25}}

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    employees = {{'name':'Jatin', 'age':35}, {'name':'Rahul', 'age':25}}
TypeError: unhashable type: 'dict'
>>> employees = {1, 2}
>>> type(employees)
<type 'set'>
>>> 
>>> names = ('Jatin', 'Aakash', 'Rahul')
>>> type(names)
<type 'tuple'>
>>> names[0] = 'Yatin'

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    names[0] = 'Yatin'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> names + names
('Jatin', 'Aakash', 'Rahul', 'Jatin', 'Aakash', 'Rahul')
>>> names * 2
('Jatin', 'Aakash', 'Rahul', 'Jatin', 'Aakash', 'Rahul')
>>> names += names
>>> names
('Jatin', 'Aakash', 'Rahul', 'Jatin', 'Aakash', 'Rahul')
>>> names *= 2
>>> names
('Jatin', 'Aakash', 'Rahul', 'Jatin', 'Aakash', 'Rahul', 'Jatin', 'Aakash', 'Rahul', 'Jatin', 'Aakash', 'Rahul')
>>> names == names
True
>>> 'Jatin' in names
True
>>> names is names
True
>>> len(names)
12
>>> tuple(employees)
(1, 2)
>>> tuple(employee1)
('salary', 'city', 'name')
>>> 
