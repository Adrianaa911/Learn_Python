# List are sequence in Python, meaning the elements inside a list can be changed!
# Assign a list to an variable named my_list
my_list = [1, 2, 3]
 
# lists can actually hold different object types. For example:
my_list = ['A string', 23, 100.232, 'o', True]
 
# len() function will tell you how many items are in the sequence of the list.
print(len(my_list))
 
#! Indexing and Slicing List
 
my_list = ['one', 'two', 'three', 4, 5]
# Grab element at index 0
print('item at index 0: ', my_list[0])
 
# Grab index 1 and everything past it
print(my_list[1:])
 
# Grab everything UP TO index 3
print(my_list[:3])
# Grab from index 2 upto index 4
print(my_list[2:4])
# We can also use + to concatenate lists, just like we did for strings.
my_list2 = ['new item1', 'new item2']
 
print(my_list + my_list2)
 
# Make the list double
print(my_list * 2)
 
# the \ => skip  it("" of'') and to use the \ we need to use \\ !!

# ? Basic List Methods
# Create a new list
list1 = [1, 2, 3]
 
# Append => add an element
list1.append('append me!')
print(list1)
 
# Pop off the 0 indexed item 
list1.pop(0)
print(list1)
 
# Use sort to sort the list (in this case alphabetical order, but for numbers it will
#  go ascending)
new_list = ['a', 'e', 'x', 'b', 'c']
print('Not sorted: ', new_list)
new_list.sort()
print('Sorted list: ', new_list)
# Use reverse to reverse order (this is permanent!)
new_list.reverse()
print('Reverse List: ', new_list)
 
#!Nesting List
 
# Let's make three lists
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]
 
# Make a list of lists to form a matrix
matrix = [lst_1, lst_2, lst_3]
print(matrix)
# Grab first item of the first item in the matrix object
print(matrix[2][2])
print(matrix[0][2])

# 1, 2, 3
# 4, 5, 6
# 7, 8, 9

breakfast = ["eggs", "cereals", "porridge"]
lunch = ["rice&chiken", "soup", "mexicano"]
dinner = ["chinese", "pasta", "fish&chips"]
meals = [breakfast, lunch, dinner]
print(meals[0][0])
print(meals[1][1])



new_list = ['a', 'e', 'x', 'b', 'c', 'm', 'f', 'g', 'h']
for my_item in new_list:
    print(my_item)
    
# https://drive.google.com/drive/folders/1WQeZQ8IQU7GGFQ1jgvuqPz-CqspRguJk?usp=sharing

day_list = ["fruits", "veggies", "water"]
week_list = ["meat", "rice", "pasta", "wine", "dairy"]
months_list = ["tissues", "oil", "petrol", "rent", "leisure centre"]
yearly_list = ["Insurrance", "Service-car", "MOT", "Annually-Tax", "Holiday"]

for the_list in months_list:
    print(the_list)
    
for own_list in week_list:
    print(own_list)
    
for for_list in day_list:
    print(for_list)
    
for all_list in yearly_list:
    print(all_list)