from collections import namedtuple
"""
experiment_id = "EXP-001"
backend = "simulator"
shots = 1000
"""

exp_tuple = ("exp-001", "tuple", 1000)
print("\nPrinting values from tuple")
print(f'Experiment_id: {exp_tuple[0]}')
print(f'Backend: {exp_tuple[1]}')
print(f'Shots: {exp_tuple[2]}')

exp_dict = {
    "experiment_id": "exp-002",
    "backend": "dictionary",
    "shots": 2000
}

print("\nPrinting values from dictionary")
print(f'Experiment_id: {exp_dict["experiment_id"]}')
print(f'Backend: {exp_dict["backend"]}')
print(f'Shots: {exp_dict["shots"]}')

Experiment = namedtuple("Exp", ["exp_id", "backend", "shots"])
exp_named_tup = Experiment("exp-003", "namedtuple", 3000)

print("\nPrinting values from namedtuple using indexes")
print(f'Experiment_id: {exp_named_tup[0]}')
print(f'Backend: {exp_named_tup[1]}')
print(f'Shots: {exp_named_tup[2]}')

print("\nPrinting values from namedtuple using field names")
print(f'Experiment Id: {exp_named_tup.exp_id}')
print(f'Backend: {exp_named_tup.backend}')
print(f'Shots: {exp_named_tup.shots}')

# creating empty tuple
try:
    exp_empty_tup = Experiment()
except TypeError:
    print("If default values are not defined, need to provide values for all attributes")

# checking immutability feature.
try:
    exp_named_tup.shots = 300
except AttributeError:
    print("Tuples are immutable")
print(exp_named_tup)

# Alternate option to copy an existing tuple to another tuple with updated values
updated_exp = exp_named_tup._replace(exp_id="exp-004",shots=400)
print(updated_exp)

# It can be used for inplace updates using the below.
updated_exp = updated_exp._replace(shots=500)
print(updated_exp)

# Copy a named tuple and update the original named tuple to see what is in both tuples.
copy_exp = updated_exp
print(f'\nCopy_exp before updating original tuple: {copy_exp}')

updated_exp = updated_exp._replace(shots=600)
print(f'\nUpdated exp after changing the value: {updated_exp}')
print(f'Copy_exp after updating original tuple: {copy_exp}')

# returns how many times "namedtuple" is present in the tuple
print(exp_named_tup.count("namedtuple"))

# returns the index of "namedtuple" if present in the tuple otherwise raises ValueError
print(exp_named_tup.index("namedtuple"))

try:
    print(exp_named_tup.index("sdfdsf"))
except ValueError:
    print(f'sdfdsf is not in {exp_named_tup}')

# retrieve all the fields in the named tuple
print(exp_named_tup._fields)

# returns the named tuple as a dictionary
new_dict = exp_named_tup._asdict()
print(type(new_dict))
print(new_dict)
new_dict["backend"] = 'dictionary'
print(new_dict)

# gives the name of fields in a tuple
print(exp_named_tup._fields)

# default values can be provided to a named tuple.
Employee = namedtuple("Employee", "name age dept paygrade", defaults=['prod', 'A1'])
emp1 = Employee("NRG", 25)
print(emp1._fields)
print(emp1._field_defaults)
print(emp1)
# Default values are assigned to the last fields when there are less number of values than the fields.

print(len(exp_named_tup))
for i in range(len(exp_named_tup)):
    print(exp_named_tup[i])

"""
Reflection:
Today I learned: How namedtuple is different from normal tuple. I have gone through the python documentation to 
understand some of the features of namedtuple. This becomes so powerful when combined with reading csv's and SQL results 

Today I struggled with: Creating test cases for this practice and a bit of understanding following goals in practice 
- iteration
- calculating total shots
- multiple records
Instead of creating functions and test cases, I have tested the features using try except exception handling. 
  
I can now write from memory: Define a namedtuple and access them using names/indexes, define default values.

One thing to repeat: I might need to check if the memory lasts after a week. I will check in the capstone project.  
"""
