from itertools import permutations


qubits = ['q0', 'q1', 'q2']
total_permutations = permutations(qubits)
# print(list(total_permutations))

for possibility in total_permutations:
    print(possibility)

two_item_permutations = permutations(qubits,2)
print(list(two_item_permutations))

one_item_permutations = permutations(qubits,1)
print(list(one_item_permutations))


# a function that accepts items and an optional permutation length and return a list of permutations
def get_permutations(items: list, length: int = None):
    if (item_length := len(items)) > 0:
        if length is None:
            length = item_length
        return list(permutations(items, length))


one_perm = get_permutations(qubits, 1)
for item in one_perm:
    print(item)

total_perm = get_permutations(qubits)
print(total_perm)

perm_empty_input = get_permutations([])
print(perm_empty_input)

more_perms = get_permutations(qubits, 4)
print(more_perms)

"""
Reflection:
Today I learned: How to generate permutations for a list of items and realised that generating permutations will grow 
exponentially by just adding one item. Generating a permutation of 10 items took around half a second. Need to be really
careful with this item. 

Today I struggled with:  Not specific to this exercise, but while defining the function, how to add the optional 
parameter. I have learnt it now

I can now write from memory: Again tested the parametrize today and it worked. It took me offgaurd when I have to pass
two inputs and one output to the test function. So far it was straight forward, one input an one output, but later 
realised, they can be passed as parameter. It is just a list of values separated by a comma.  

One thing to repeat: I might need to check if the memory lasts after a week. I will check in the capstone project.  
"""
