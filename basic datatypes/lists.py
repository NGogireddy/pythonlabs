print("This is all about lists")

"""
List is like an array except that it can be expanded, contracted or hold different objects
"""

num_list = [100,1,2,3,4,5,6,7]

# Other ways of creating a list.
char_list = list('abcdef')
empty_list = []
iterable_list = [x for x in 'pqrs']

# Below is also a list.
obj_list = [num_list,char_list,'xyz',3.14,'etc']

print(num_list)
print(char_list)
print(obj_list)
print(iterable_list)
print(empty_list)
print("\n")
"""
Lists can be accessed using indexes and slicing
"""
print("Following are some of the ways to access items in a list")
print(num_list[0])
print(obj_list[-1])
print(num_list[1:4])
print(char_list[1:])
print(obj_list[0][2])
# The above works when we have a list within another list. obj_list[3][1] will not work. obj_list[3] is an integer.
print("\n")

"""
Methods in List class 
"""
num_list.reverse()
print(f"num_list is reversed now {num_list}")

print(f"Number of occurances of 5 in num_list is: {num_list.count(5)}")
print(f"Popped the last object from num_list: {num_list.pop()}")
print(f"num_list after the pop is {num_list}")
print("\n")

print(f"Popping an object at index 3 : {num_list.pop(3)}")
print(f"num_list after the pop is {num_list}")
num_list.sort()
print(f'Sorted the numlist {num_list}')
char_list.sort(reverse=True)
print(f'Sorted char_list in reverse order : {char_list}')
print("\n")

num_list.append(8)
print(f'num_list after appending 8 is :{num_list}')
# num_list.clear() to clear all the objects in num_list
num_list.extend([9,10,11])
print(f'Extended num_list after adding 9, 10, 11 is {num_list}')
num_list.insert(3,4)
print(f'Inserted number 4 after 3rd position. Now list is {num_list}')

iterable_list.reverse()
print(f'iterable_list is reversed {iterable_list}')

