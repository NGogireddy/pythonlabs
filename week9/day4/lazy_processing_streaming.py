"""
## Drill
Compare these two ideas:

-   create a complete list of transformed values
-   produce each transformed value only when requested

Predict which one retains all results at once.

The first one retains all the results at once as it has to create a complete list which needs to store all the results
at once. In the second one we are producing the results only when needed. This need not store all the results at once,
when requested it can transform the first element and then wait for the next request to just transform the next item.

"""


def eager_version_squares(orig_list):
    """
    returns the list of squares of all numbers in the list
    :param n: list of numbers
    :return: list of squares of the numbers
    """
    return [num**2 for num in orig_list if isinstance(num, (int, float))]


def lazy_version_squares(orig_list):
    """
    yields the squares of first n natural numbers
    :param n: Positive integer
    :return: yield square numbers
    """
    for num in orig_list:
        if isinstance(num, (int, float)) and not isinstance(num, bool):
            yield num**2


"""
> Does a generator guarantee that an entire program uses little memory? Why or why not?

No. A generator can reduce memory use when it produces values one at a time instead of building a whole collection in 
memory. But it doesn’t guarantee that the entire program uses little memory: other parts of the program may store large 
lists, caches, or results, and a generator may itself retain references to data while it runs.
Generators can make a particular data-processing step more memory-efficient, depending on how they’re used.
"""
