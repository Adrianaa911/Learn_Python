# DICTIONARY : UPDATE AND DELETE a data 

# we use dictionaries in situation where we wan to to store information as key values pairs
# two ways for creating dictionary in python
# The first way is by using a set of curly braces, {}, and the second way is by using the built-in dict() function.
customer = {
    "name": "Zak Pardis",
    "age": 28,
    "bachelor": True,
    "location": "London"
}
 
print(customer["name"])  # Zak Pardis
# print(customer["birth_date"])  #! will drop an error as the key is not exist.
# we can use get method as well to return value of a key
print(customer.get("name"))  # Zak Pardis
 
# will return None instead of error
# None is an object which represent absence of a value
print("Key is not available: ", customer.get("birth_date"))
 
print(customer.get("birth_date", "Jan 1 1995"))  # Jan 1 1995
 
customer["name"] = "John Smith"  # will update value on the name key
customer["birth_date"] = "Jan 1 1995"  # will add new key value pair
print(customer)
# Creating a dictionary
student = {
    "name": "Alice",
    "age": 18,
    "grade": "A"
}
 
# Accessing values by key
name = student["name"]  # Retrieves "Alice"
age = student["age"]    # Retrieves 18
 
# How to View All values
print(student.values())  # dict_values(['Alice', 18, 'A'])
# How to View All keys
print(student.keys())  # dict_keys(['name', 'age', 'grade'])
# Modifying the "age" value
student["age"] = 19  # Updates age to 19
# Adding a new key-value pair
student["city"] = "New York"
 
# Deleting a key-value pair
del student["grade"]  # Removes the "grade" key and its associated value
 
# Checking for key existence:
# - Using the in operator:
# Checking if a key exists
if "age" in student:
    print("student has age field")
else:
    print("Student doesn't have age field")
 
 
if "age" in student:
    print("Age exists:", student["age"])
else:
    print("Age does not exist")
 
# - Using the get() method:
 
print(student.get("grade", "Not Exist"))
 
grade = student.get("grade", "N/A")
# If "grade" exists, it retrieves the value; otherwise, it returns "N/A"
# Exploring built-in dictionary methods:
# `keys()`: This method returns a view object that displays a list of all the keys in the dictionary.
# Example
student = {
 
    "grade": "B",
    "lastName": "Mistodi",
    "name": "Adriana",
    "bachelor": True,
    "marriage": False,
    "location": "East London",
    "age": 20
}
keys = student.keys()  # Returns a view object of keys
print(keys)
# `values()`: Similar to keys(), this method returns a view object that displays a list of all the values in the dictionary.
# Example
values = student.values()  # Returns a view object of values
print(values)
# `items()`: This method returns a view object of all key-value pairs in the dictionary as tuples.
# Example
items = student.items()  # Returns a view object of (key, value) pairs
print(items)
# Sorting and iterating through dictionaries:
# Sorting a dictionary by keys
sorted_keys = sorted(student.keys())
# sorted_value = sorted(student.values())
# print(sorted_value)
 
for key in student:
    value = student[key]
    print(f"{key}: {value}")
 
for data in student:
    print(f"{data}: ", student[data])