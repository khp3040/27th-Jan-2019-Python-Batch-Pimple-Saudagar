Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> string = 'This is my sample string'
>>> string[0:4:1]
'This'
>>> string[0:4:2]
'Ti'
>>> string[0:4:3]
'Ts'
>>> string[0:4] # default step is 1
'This'
>>> string[:4] # default start is 0
'This'
>>> string[:] # default end is len(object)
'This is my sample string'
>>> string[-4:] # default end is len(object)
'ring'
>>> string[-1:-7:-1] # default end is len(object)
'gnirts'
>>> string[-1:-7] # default end is len(object)
''
>>> 
>>> name = 'nitin'
>>> name == name[-1::-1]
True
>>> name[-1::]
'n'
>>> name[-2:-1]
'i'
>>> 
>>> 
>>> number = 12345
>>> str(number)[0]
'1'
>>> str(number)[-1]
'5'
>>> int(str(number)[-1] + str(number)[1:-1] + str(number)[0])
52341
>>> str(number)[-1] + str(number)[1:-1] + str(number)[0]
'52341'
>>> 
>>> employee1 = [1, 'Jatin', 'Pune', 20000, 'IT']
>>> type(employee1)
<type 'list'>
>>> employee1[2]
'Pune'
>>> employee1[2:1]
[]
>>> employee1[2:1:-1]
['Pune']
>>> employee1[0] = 2 # ??
>>> employee1
[2, 'Jatin', 'Pune', 20000, 'IT']
>>> employee1[5] = 10

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    employee1[5] = 10
IndexError: list assignment index out of range
>>> employee1[6]

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    employee1[6]
IndexError: list index out of range
>>> len(employee1)
5
>>> # Airthmaric Opr + , *
>>> employee1
[2, 'Jatin', 'Pune', 20000, 'IT']
>>> employee1 + employee1
[2, 'Jatin', 'Pune', 20000, 'IT', 2, 'Jatin', 'Pune', 20000, 'IT']
>>> employee1 * 2
[2, 'Jatin', 'Pune', 20000, 'IT', 2, 'Jatin', 'Pune', 20000, 'IT']
>>> # Assignment +=, *=
>>> employee1 += employee1
>>> employee1
[2, 'Jatin', 'Pune', 20000, 'IT', 2, 'Jatin', 'Pune', 20000, 'IT']
>>> # comparison
>>> 
>>> employee2 = [1, 'Rahul']
>>> employee1
[2, 'Jatin', 'Pune', 20000, 'IT', 2, 'Jatin', 'Pune', 20000, 'IT']
>>> employee2
[1, 'Rahul']
>>> 
>>> employee1 > employee2
True
>>> len(employee1) > len(employee2)
True
>>> employee2 = [2, 'Rahul']
>>> employee1 > employee2
False
>>> 
>>> employee1
[2, 'Jatin', 'Pune', 20000, 'IT', 2, 'Jatin', 'Pune', 20000, 'IT']
>>> employee2 = employee1
>>> id(employee1)
4377934664
>>> id(employee2)
4377934664
>>> employee1
[2, 'Jatin', 'Pune', 20000, 'IT', 2, 'Jatin', 'Pune', 20000, 'IT']
>>> employee2
[2, 'Jatin', 'Pune', 20000, 'IT', 2, 'Jatin', 'Pune', 20000, 'IT']
>>> employee1[0] = 10
>>> employee2 #?
[10, 'Jatin', 'Pune', 20000, 'IT', 2, 'Jatin', 'Pune', 20000, 'IT']
>>> 
>>> employee1 is employee2

