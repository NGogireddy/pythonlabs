from itertools import combinations


qubits = ["q0", "q1", "q2", "q3"]

unique_combinations = combinations(qubits, 1)
for combination in unique_combinations:
    print(combination)

unique_pairs = combinations(qubits, 2)
print(list(unique_pairs))

unique_triples = combinations(qubits, 3)
print(list(unique_triples))


# function to accept a list and optional parameter to return the list of unique combinations
def get_unique_combinations(input_list: list, length: int = None):
    try:
        if (item_length := len(input_list)) > 0:
            if length is None:
                length = 1
            return list(combinations(input_list, length))
    except (TypeError, ValueError):
        raise ValueError("length must be a positive integer")


print(get_unique_combinations(qubits))
print(get_unique_combinations(qubits, 0))
print(get_unique_combinations(qubits, 2))
print(get_unique_combinations(qubits, 3))
print(get_unique_combinations([1, 2, 2, 2, 3], 2))
try:
    print(get_unique_combinations(qubits, -3))
except ValueError as e:
    print(str(e))


"""
Reflection:
Today I learned: How to generate combinations for a list of items and understood the difference between a permutation 
and combination. If the input provided to combinations iterable has duplicate values, it will not remove them i.e, it 
treats each item in the list uniquely.

Today I struggled with:  Nothing specific

I can now write from memory: Test cases for scenarios where exceptions are raised i.e with pytest.raises.  

One thing to repeat: I have realised that I need to repeat the fixture syntax, I am sure I will practice in due course.  
"""
