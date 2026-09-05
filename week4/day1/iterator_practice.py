"""
iterable: A python object that implements __iter__(), it actually holds all the items that you can iterate
iterator: The tool to iterate through the iterable items. It implements __next__().
iteration: The process of iterating through the items in iterable.
"""

""" Drill 1
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator)) --> 10
print(next(iterator)) --> 20
print(next(iterator)) --> 30
"""

""" Drill2
numbers = [10, 20]
iterator = iter(numbers)

print(next(iterator)) --> 10
print(next(iterator)) --> 20
print(next(iterator)) --> Index/Memory Error (Actually StopIteration error)
"""

""" Drill3
numbers = [1, 2, 3]
iterator = iter(numbers)

for number in iterator:
    print(number) --> prints 1 2 and 3 in each line

print(next(iterator)) --> StopIteration Error

The for loop exhausted all the items in the iterator, calling next will raise StopIteration Error
"""

class InputError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


def consume_first_n(iterable, n):
    """
    returns the first n values from the iterable as list. If first argument is not iterable raises InputError, if n is 0
    or negative, returns empty list. If n is more than total number of items then raises InputError
    :param iterable:
    :param n:
    :return: list
    """
    return_list = []
    try:
        for _ in range(n):
            return_list.append(next(iterable))
        return return_list
    except TypeError as e:
        raise InputError(str(e))
    except StopIteration:
        raise InputError("Requested items more than iterable contents")

"""
### Engineering question

Would you implement this using: list(iterable)[:n] or by consuming the iterator incrementally? Explain your choice.

No, I will not use list(iterable)[:n] as this will first loop through all the iterables and loads everything into 
memory then gives the first n numbers. It is slow and memory inefficient. 
"""

"""
Reflection: 
1. What is the difference between an iterable and an iterator?
iterable is object through which we can loop and iterator is the tool to iterate all the items. 

2. What state does an iterator maintain?
iterator is kind of an index and it understands the current value of the iterable can fetch the next values. 

3. Why is converting everything to a list sometimes undesirable?
When the list is huge it can crash the memory and slow down the processing. 
 
4. What did you choose for negative `n`, and why?
I chose to return empty list as the user doesn't want anything more than 0. 

Learning: 
1. list, tuple, string, set, dictionary on their own are not iterables. we have to create an iterator and 
use the iterator to iterate. 
2. when we define an iterator on a dictionary it will iterate through the keys. 
3. All testing is done through test cases today and I haven't referred my previous exercises to write the test cases. 
4. I haven't forced myself to fit fixture/tmp_path in the test cases. 
"""