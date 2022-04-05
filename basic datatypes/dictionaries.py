print("Dictionaries illustrated with python")
print("Dictionary is an unordered set of key value pairs")
print("values can be accessed if we know the specific key")

cost_price = {'apple':1.5,'grapes':2.0,'kiwi':0.6}

for k in cost_price.keys():
    print(f"Cost of {k} is {cost_price[k]}")

# We can add new key value pair to the dictionary using a simple assignment
cost_price['bananas'] = 1.0
print(cost_price)
print("\n")

print("The values need not be of same dataype for all the keys")
student = {'name':'Jose','age':25,'languages':['C','python','AWS']}
print(student)
print(student['languages'])

print("A dictionary can have another dictionary inside it")
student['certifications'] = {'Java':'OCJP certified Developer','AWS':'Architect certified'}
print(student)
print(student['certifications']['Java'])
print("!!! Note keyerror is raised when the key is not present in the dictionary. ")
print("\n")

print(f'Get a list of keys using .keys() method {student.keys()}')
print(f"Get a list of values using .values() method {student.values()}")
print(f"Another way of getting the value using .get() method {student.get('name')}")
print(f"Remove a key value pair using pop() method {student.pop('age')}")
print(f"Another option to remove a key is 'del student['age']'")
print(f"student dictionary after the pop is :\n {student}")
print(f"'age' in student checks if the key 'age' is present in student: {'age' in student}")
print(f"'group' not in student checks if the key 'group' is not present in student: {'group' not in student}")
print("\n")

print("Making some copies of student dictionary")

# Two ways of copying a dictionary to another variable.
student2 = student.copy()
student3 = student2
print(f"{student2}")
print(f"{student3}")
print('With direct assignment using = both the variables refer to the same object. Changes to student2 can be seen in student3')

student2['age']=30
print(f"Student3 after adding age to student2 : {student3}")
print("\n")
print(f"Cleared the student3 using clear() method {student3.clear()}")
print(f"Student3 after the clear : {student3}")

print(f"Printing items in the dictionary {student.items()}")
print("items() method returns a list of tuples. Each tuple is a key value pair")
print("\n")

print("popitem() method returns the last inserted key value pair as a tuple")
print(student.popitem())
print("above item is popped from the dictionary and we are adding age to pop it again")
student['age'] = 25
print(student.popitem())
print("Age is added and then popped. Latest student will not have age.")
print(student)
print("!!!!!! This functionality will help in implementing LIFO (Last In First Out) algorithms !!!!!!")

print(f"list(student) returns a list of all keys in student {list(student)}")
print(f"len(student) returns the count of values in student {len(student)}")
print(f"iter(student) returns an iterable on keys of student {iter(student)}")
print("\n")

print("A new dictionary can be created with the same keys in current dictionary but different values.")
values = ' '
studentx = student.fromkeys(iter(student),values)
print(studentx)
print(student)

print("get() method takes key as mandatory argument and optional default value to return if the key is not present")
print(student.get('group','Computers'))
print(student.get('name','Default Name'))

print("reversed(student) returns a reversed iterable on keys of student")
print(f"student.setdefault('name','Default') returns the value of name if present {student.setdefault('name','Default')}")
print(f"student.setdefault('group','Computer') adds group key to dictionary and returns the value {student.setdefault('group','Computers')}")
print(f'student after adding group {student}')

print("\n")
studentx.update(student)
print(f'studentx is updated with student data using the command studentx.update(student). Now studentx is {studentx}')
