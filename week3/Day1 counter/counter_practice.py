from collections import Counter

# Solving the frequency counting problem wihtout counters

states = ["00", "11", "00", "01", "11", "00"]

freq_dict = {}

for state in states:
    if state in freq_dict:
        freq_dict[state] += 1
    else:
        freq_dict[state] = 1

print(freq_dict)

# Solving this problem using counters

freq_counter = Counter(states)

print(freq_counter)
print(type(freq_counter))

states.append('10')
print(states)
freq_counter.update(states)
print(freq_counter)

# update function adds to the existing counters. It adds everything given as parameter, not just the latest appended items.

freq_counter.update(['001', '010'])
print(freq_counter)

print(freq_counter.most_common(2))
print(type(freq_counter.most_common(2)))

print(freq_counter.most_common(1))
print(freq_counter.most_common(10))
print(freq_counter.most_common(-2))
print(Counter(['abc', 1, 2.5]))

# most_common method returns a list of most frequent counters and their frequencies in the form of a tuple.
# It takes an integer argument and returns that many results. If the integer is negative an empty list is returned.
# It will not throw index out of bounds if the requested number is more than the keys in the counter
# The list passed to the counter function should not have iterables like list, set, dictionary etc.


def count_states(states):
    counts = Counter(states)
    return counts


def get_most_common(states):
    if output := count_states(states).most_common(1):
        return output[0][0]


# most_common(1) returns the most frequent value, if two or more has same frequency,
# it returns the first item in the list of all the high frequency item.

print(count_states([2, 3, 4, 5, 2, 1, 3]))
print(count_states([]))

print(get_most_common([2, 3, 4, 5, 2, 1, 3]))
print(get_most_common([]))

"""
Reflection: 

Today I learned: concept of counter and how helpful it is to get the most common, unique states. 
Today I struggled with: passing the counter parameter in parameterize, later I learnt to use dictionary 
I can now write from memory: The parameterize of pytest.
One thing to repeat: Not to repeat but muscle memory syntax of Counter and explore other features of counter

"""