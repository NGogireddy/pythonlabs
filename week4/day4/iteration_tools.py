from itertools import islice

"""
Drill 1

Rewrite:

index = 0
for result in results:
    print(index, result)
    index += 1

using the appropriate built-in.
"""

print("Demonstration of enumerate: ")
results = [10, 15, 23, 12, 14, 16]

for index, result in enumerate(results):
    print(index, result)

"""
Drill 2

Rewrite:
for i in range(len(states)):
    print(states[i], counts[i])
using the appropriate built-in.
"""
print("\nDemonstration of zip: ")
states = ['00', '01', '10', '11']
counts = [100, 213, 218, 239, 400, 300, 50, 70]
for state, count in zip(states, counts):
    print(state, count)

"""
Drill 3

Given: results = range(1_000_000)
How would you process only the first 10 values without creating: list(results)[:10]

"""

print("\nDemonstrating islice:")

results = range(1_000_000)
for a in islice(results, 5):
    print(a)

"""
Understand:
- why `range(len(...))` is often unnecessary
    We can use enumererate which will give attach an index to all the items in the iterable, the length is automatically
    calculated here. 
     
- how `zip()` behaves with different lengths
    Zip actually stops when the shortest iterable is exhausted. 
    
- how `islice()` differs from normal slicing
    slice creates a list of original items with the requested number, it needs the whole list of items before slicing. 
    islice produces lazily and works on any iterable, works best when paired with generator. 
    
- why iterators cannot always be sliced using `[:]`
    If iterators should be sliced using [:], it should know what are all the items present in the iterator i.e, a list 
    should be provided before slicing. 
"""


def pair_results(states, counts):
    """
    It pairs the results to the counts and returns a list of tuples. It stops when one of the list is exhausted.
    :param states: A list of quantum qubit states
    :param counts: A list of counts from the experiment.
    :return: list of tuples.
    """
    return list(zip(states, counts))


def first_n_results(results, n):
    """
    Give the first n results from iterable, if n is 0 return empty list, if n > number of iterables return all items in
    iterables and stop.
    :param results: iterable
    :param n: number of results to be returned.
    :return: list of n results
    """
    return list(islice(results, n))


"""
## Reflection

1. Why is `enumerate()` preferable to manually maintaining an index?
enumerate is a lazy iterator which is efficient whilst processing huge data and maintaining index is an overhead.  

2. What happens when two inputs to `zip()` have different lengths?
It stops iterating after the smallest input is exhausted.

3. Why is `islice()` useful for iterators?
islice is lazy iterator, it is efficient in memory and works with all types of iterators. 

4. Which of today's tools do you expect to use most often?
All of the tools has their own merit and use case, I believe islice and enumerate are going to be mostly used. I may be
wrong, it all boils down to the problem we are solving. 

"""