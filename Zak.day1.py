# single comment
"""
multi line
comment
"""
 
print("First Day of Python")
# input() - get input from user
 
# variable => Labels for memory location
name = "Zak"
age = 28
 
print(type(age))
salary = 10.5
print(type(salary))  # float
 
# !Python DataTypes
'''
Numeric -   int, float, complex
String -    str
Sequence -  list, tuple, range, str
Binary -    bytes, bytearray, memoryview
Mapping -   dict
Boolean -   bool
Set -       set, frozenset
None -      NoneType
'''
 
 
# Numeric Data type
 
value1 = 10
value2 = 20
print(value1+value2)
print(value1*value2)
 
# String
name = "Adriana Mistodi"
#!String
# String
# To create a string in Python you need to use either single quotes or double quotes. For example:
 
# !Single word
print('hello')
 
# !Entire phrase
print('This is also a string')
 
# !We can also use double quote
print("String built with double quotes")
 
#! Be careful with quotes!
print(' I\'m using single quotes, but this will create an error')
 
# ? We can also use a function called len() to check the length of a string!
print(len('Hello World'))
 
"Now I'm ready to use the single quotes inside a string!"
 
# String Indexing
# ? We know strings are a sequence, which means Python can use indexes to call parts of the sequence. Let's learn how this works.
 
# ? In Python, we use brackets <code>[]</code> after an object to call its index. We should also note that indexing starts at 0 for Python. Let's create a new object called <code>s</code> and then walk through a few examples of indexing.
var = "HELLO PYTHON"
print("var:", var)
print("var[3:8]:", var[2:4])  # LL
print("var[-9:-4]:", var[-9:-4])  # LO PY
del var
print(name[0:7])  # [inclusiveIndex:exclusiveIndex]
print(name[3:5])
print(name[0:])
print(name[-7:])
 
first_name = input("What is your first Name? ")
last_name = input("What is your last name? ")
age = int(input("What is your age? "))
 
# print(last_name+' '+first_name)
# print('{} {}'.format(first_name, last_name))
print(f"{first_name} {last_name}")  # string interpolation
print(f"Your full name is {first_name} {last_name} and your age is {age}")
 
# List and Dictionary