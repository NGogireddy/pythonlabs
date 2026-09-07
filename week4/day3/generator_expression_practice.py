"""
Compare:
[x * 2 for x in numbers]

with:
(x * 2 for x in numbers)

The first one is a list of doubles for all the items in the numbers.
The second one is a generator expression. It will only return one item at once, next item should be retrieved using next

"""

list_squares = [x**2 for x in range(1, 11)]
print(list_squares)

square_generator = (x**2 for x in range(1,11))
print(square_generator)   # prints the generator object not the values.
print(next(square_generator))  # prints the first item of the generator.
for square in square_generator:  # printing the remaining squares one at a time.
    print(square)

"""
## Drill — Predict Memory Behaviour

Identify whether each expression creates the entire result immediately or produces values lazily:
[x * 2 for x in range(10)]   (x * 2 for x in range(10))
As demonstrated above the list comprehension generates all the results at once and stores in the memory. The generator 
expression lazily produces the next item and efficient when working with huge volumes.

Why does this not require a million-element result list?

sum(x * 2 for x in range(1_000_000))

sum needs two arguments and the above generator adds the first two numbers stores the result and takes the next number 
and adds it to the result. This repeats until the last number is generated lazily.
"""


def get_valid_counts(results):
    """
    Validates results and yields the count for all the valid results
    :param results: list of result records
    :return: valid counts
    """
    for result in results:
        if "experiment_id" in result and "state" in result and "count" in result:
            if isinstance(result["experiment_id"], str) and isinstance(result["state"], str) and isinstance(result["count"], int):
                if result["count"] > 0:
                    yield result["count"]


def sum_valid_counts(results):
    return sum(count for count in get_valid_counts(results))


"""
Reflection: 
I struggled a little bit understanding the assignment in the given context. Used google for better explanation.
The implementation is completely on my own.  I was also struggling to implement the list comprehension in the solution, 
but later implemented that in the test cases. I have given an input of the lists and get_valid_counts yields the valid 
counts. I have used the list comprehension there to collect all the valid counts and assert it.  

1. When would you prefer a list comprehension?
I will use it when I am certain that the resulting output is small or when the result of the expression should be parsed
more than once for e.g, finding sum, avg and std deviation for all the items. 

2. When would you prefer a generator expression?
It should be used when there is only one iteration required for the items and it is huge in size. 

3. What does “lazy” mean in practical terms?
It is processed only when required and discarded once processed. 

4. Did using a generator actually improve the solution, or did you use it just because this is Generator Week?
It definitely improves the solution and is needed for practical implementation purpose. List comprehension is not the 
one solution fits all. 
"""
