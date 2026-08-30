from collections import defaultdict

records = [
    ("simulator", 100),
    ("hardware", 200),
    ("simulator", 150),
    ("hardware", 300),
]

# grouping shots by backend without using defaultdict.
grouped_shots = dict()

for key, value in records:
    if key not in grouped_shots:
        grouped_shots[key] = []
    grouped_shots[key].append(value)

print(grouped_shots)
grouped_shots2 = grouped_shots.copy()
print(grouped_shots2)

shots = defaultdict(list)
print(shots)

for key, value in records:
    shots[key].append(value)

print(shots)

print(shots['simulator'])
print(shots['invalid'])   # --> doesn't raise KeyError, instead adds the key to the defaultdict

shots2 = shots.copy()
print(shots2)
print(shots2.values())
print(shots2.keys())
print(shots2.setdefault('new_key',0))   # adds this key value if not present in defaultdict, can give different type of
# value other than the initial default typei.e, int, float, string but it is not a good practice
print(shots2)
print(shots2.setdefault('simulator',0))   # returns the value if key is present, will not replace with default
print(shots2.pop('new_key'))   # Key provided should be present in defaultdict, else you get KeyError
print(shots2)
shots2.clear()   # clears everything in the dictionary
print(shots2)

# All methods in the defaultdict work similar to dictionary except that KeyError will not be raised when indexing a new
# key (exception pop)


def group_by_backend(records):
    group = defaultdict(list)
    for key, value in records:
        group[key].append(value)
    return group


def total_shots_by_backend(records):
    grouped_shots = group_by_backend(records)
    total_shots = defaultdict(int)
    for key in grouped_shots.keys():
        for count in grouped_shots[key]:
            total_shots[key] += count
    return total_shots


"""
Why is: groups[key].append(value) often clearer than repeatedly checking:
if key not in groups:
    groups[key] = []

Answer: When the size of the dictionary is huge "key not in groups" check reads all the key in the dictionary, which 
reads a lot of content before finding it is not present and then initialize it before appending the value, memory and 
performance take a hit here. 

Today I learned: How a defaultdict is much better and easier to use than the dictionary
Today I struggled with: Nothing much. I have realised that when value is a list in a dictionary i cannot unpair using 
key, value in a for loop. 
I can now write from memory: pytest for parametrize
One thing to repeat: None for today. 
"""
