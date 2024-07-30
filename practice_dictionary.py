id = {
    "name": "James",
    "surname": "Bond",
    "age": 37,
    "address": "11 Margate road",
    "city": "London",
    "proffession": "Bank Director",
    "bachelor": True 
}
print(id["name"])
print(id["surname"])
print(id["age"])
print(id["address"])
print(id["city"])
print(id["bachelor"])

# Another method
print(id.get("proffession"))
print(id.get("city"))


# This method add up a new record
print(id.get("date_of_birth", "11-07-1984"))

id["name"] = "Alicia"   # will update value on the name key
id["birthDate"] = "3 November 1992"  # will add new key value pair

print(id["name"])
print(id["birthDate"])
print(id)

# Creating a dictionary
book = {
    "title": "Twilight",
    "author": "Stephanie Mayer",
    "year": 2007,
    "genre": "fiction"
}

# Accessing value by key
author = book ["author"]
title = book ["title"]
print(book)

# How to view all values
print(book.values())

# View all keys
print(book.keys())

# Modify the "year" value
book["year"] = 2010  #update year to 2010
print(book)

# Adding a new key-value pair
book["city"] = "New York"
print(book)

# Deleting a key-value pair
del book["genre"]  #removes the "genre" key and it's value
print(book)

book["town"] = "London"
print(book)

if "town" in book:
    print("Town is a field in the book records.")
else:
    print("Town doesn't exist in the book records!")


# Checking for key existence:
  # using the ' in ' operator
if "title" in book:
    print("Title is a record in book!") 
else:
    print("Title isn't a field in book!")
    
if "author" in book:
    print("Author exist: ", book["author"])
else:
    print("Author doesn't exist")
    
if "year" in book:
    print("Year exist in the field.")
else:
    print("Year do not a field!")
    
if "apperence" in book:
    print("Apperence exist in the field.")
else:
    print("Apperence doesn't not exist in the field! ")    
    
if "rating" in book:
    print("The rating exist in the field.")
else:
    print("Rating do Not exist in the book field!")
    
    
# Using the .get() method
print(book.get("grade", "Not exist"))
print(book.get("title", "N/A"))
print(book.get("grade", "N/A")) # if 'grade' exist will retrieves the value of it, otherwise will return N/A
print(book)
print(book["author"])

# Exploring build-in dictionary method:
  # # `keys()`: This method returns a view object that displays a list of all the keys in the dictionary.
# Example1

member = {
    "name": "Adriana",
    "surname": "Mistodi",
    "grade": "A",
    "bachelor": True,
    "marriage": False,
    "age": 31,
    "location": "London",
    "status": "Happy"
}
keys = member.keys() #returns a view object of keys
print(keys)

# `values()`: Similar to keys(), this method returns a view object that displays a list of all the values in the dictionary.
values = member.values()
print(values)

# Example 2

history = {
    "original": "Romania",
    "current": "London",
    "situation": "Stabil",
    "future": "USA"
}
keys = history.keys()
print(keys)

values = history.values()
print(values)

# `items()`: This method returns a view object of all key-value pairs in the dictionary as tuples.
# Example
items = member.items()
print(items)
items = history.items()
print(items)
items = book.items()
print(items)
items = id.items()
print(items)


# Sorting and iterating through dictionaries
  # Sorting a dictionary by keys
sorted_keys = sorted(member.keys())
print(sorted_keys)
  
  # Sorting a dictionary by values
#sorted_values = sorted(book.values())
#print(sorted_values)

for key in id:
    value = id[key]
    print(f"{key}: {value}")
    
for key in book:
    value = book[key]
    print(f"{key}: {value}")
    
for key in member:
    value = member[key]
    print(f"{key} : {value}")
    
for key in history:
    value = history[key]
    print(f"{key}: {value}")
    



for data in id:
    print(f"{data}: ", id[data])
    
for data in book:
    print(f"{data}: ", book[data])
    
for data in member:
    print(f"{data}: ", member[data])
    
for data in history:
    print(f"{data}: ", history[data])
