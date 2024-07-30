# single comment
    
"""_summary
 multi line comment_
"""
print("First Day of Python")
#input() - get input from user

# variable => labels for memory location, where the data is located
name="Adryana"
age=28
surname = "Mistodi"

print(type(name))
print(type(surname))
print(type(age))

salary= 200.5
print(type(salary)) #float: big and split numbers, decimal

# !Python DataTypes!!
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

#Numeric Data Type

value1=10
value2=20
print(value1+value2)
print(value1*value2)

#String
name="Adriana Mistodi"
print(name[0:7]) # [inclusive Index: Exclusive]
print(name[3:5])
print(name[0:])
print(name[-7:]) # negative means selects from right side, opposite side#!String
# Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.
value = "The type of variable having value"
print(value[0:6])  # The ty
print(value[:6])  # The ty
print(value[0:])  # The type of variable having value
print(value[:])  # The type of variable having value
print(value[-5:])  # value
print(value * 2)  # Prints string two times


first_name = input("What is your first name?")
last_name=input("What is your last name?")
age=int(input("What is your age?"))
address=input("Where do you live?")
occupation=input("What's your occupation?")
job=input("What's your dream job?")
travel = input("Where would you like to travel? ")

#print(first_name + ' ' +last_name) # one way
print('{} {}'.format(first_name, last_name)) #another method
print(f"{first_name} {last_name}") # string interpolation - another way
print(f"Your full name is: {first_name} {last_name} and your age is: {age}")
print(f"Your full name is: {first_name} {last_name} and your age is: {age+1}")
print(f" You are: {first_name+ ' ' +last_name}, your age is: {age}, you live in: {address}, your dream job is: {job} and you would like to visit: {travel} ")



# Python variables are case sensitive which means Age and age are two different variables:
COUNTER = 100          # Creates an integer variable
Miles = 1000.0       # Creates a floating point variable
Name = "Zara Ali"   # Creates a string variable
 
print(COUNTER)
print(Miles)
print(Name)
 
# !Deleting Python Variables
# You can delete the reference to a number object by using the del statement.
del Miles
# print(miles)  # will produce error - as it is deleted.
del COUNTER, Name
 
# !Getting Type of a Variable
name = "Zak"
print(type(name))  # <class 'str'>




#List and Dictionary