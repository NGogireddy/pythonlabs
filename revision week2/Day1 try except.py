# Muscle memory Practice
try:
    # code which can fail at run time
    number = 'asdf'
    raise ValueError
except ValueError:
    # What should I do if the ValueError is caught.
    print("ValueError is raised")

# Muscle memory exercise converting a number to float:
value = 4
try:
    floating_value = float(value)
    print(f"Floated value is : {floating_value}")
except ValueError:
    print(f'Cannot convert "{value}" into float')

# Type error
age = 24
try:
    age_line = "I am " + age + "years old"
except TypeError:
    print("Cannot convert int to string implicitly")

# example of zero division error
a, b = 5, 0
try:
    print(a/b)
except ZeroDivisionError:
    print(f'Divisor cannot be 0')

# file not found error
try:
    with open('file.txt', 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"file.txt not found")

# example for Key error
name_dict = {"Alice": 123, "Bob": 456}
key = "Charlie"
try:
    print(name_dict[key])
except KeyError:
    print(f"Key {key} not found in names")

# example of IndexError
nums = list(range(5))
try:
    print(nums[6])
except IndexError:
    print(f"nums doesn't have index : 6")

# sensor_reader.py
sensor_reading = input("Enter sensor reading : ")
try:
    floating_value = float(sensor_reading)
except ValueError:
    print(f'Sensor reading should be a number')

# Quantum style validation
quantum_input = input("Enter a quantum value : ")
try:
    q_i = float(quantum_input)
    if 0 <= q_i <= 1:
        print("Valid value")
    else:
        print("Invalid value")
except ValueError:
    print(f"{quantum_input} is not a number")

# Difference between exception caused by python and business rule.
"""
Exceptions from Python are raised when universal rules fail i.e, when someone is trying to access an Index that is not 
in the list or trying to convert a name to a number, dividing something with zero, adding integers with dictionaries etc.

Business rules are something that are domain specific. They are technically correct but not valid in the context of a 
business. Eg: Interest rate cannot be more than 50%. Interest rate cannot be negative. Post code cannot be more than 9 
characters and cannot have any special characters etc,  
"""
