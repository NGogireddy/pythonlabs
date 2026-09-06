import inspect

"""
explain why:

def numbers():
    yield 1
    yield 2
    yield 3

does not immediately execute the body like a normal function call.

Ans: numbers is a generator function, it generates the first output and returns the control to the calling method. When
next item is required, it resumes the execution and returns the next item along with the control. This process repeats
until there are no more items to yield and StopIteration is hit.

"""

"""
Drill — Predict the Execution

def generate_numbers():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

generator = generate_numbers()

print("A")
print(next(generator))
print("B")
print(next(generator))
print("C")

Prediction:
A
Start
1
B
middle
2
C

"""


def generate_numbers():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")


generator = generate_numbers()

print("A")
print(next(generator))
print("B")
print(next(generator))
print("C")

"""
Result: The prediction is correct. 
"""

"""
Study: 
I have gone through all the items and learnt about generator state. The remaining concepts were same as my understanding
"""


def state_demo():
    yield "First item"
    yield "Second item"


gen = state_demo()

print(inspect.getgeneratorstate(gen))
print(next(gen))
print(inspect.getgeneratorstate(gen))
print(next(gen))
print(inspect.getgeneratorstate(gen))
try:
    print(next(gen))
except StopIteration:
    print(f"Nothing to yield. Status of gen is {inspect.getgeneratorstate(gen)}")

# Once an item is generated (including last) the generator state goes into GEN_SUSPENDED state. If we do a next after
# the last item it raises StopIteration and state changes to GEN_CLOSED.


def state_demo2():
    yield "First item"
    return
    yield "Second item"


gen2 = state_demo2()

print(inspect.getgeneratorstate(gen2))
print(next(gen2))
print(inspect.getgeneratorstate(gen2))
try:
    print(next(gen2))
except StopIteration:
    print(f"Nothing to yield. Status of gen is {inspect.getgeneratorstate(gen2)}")

# Once a return statement is encountered in the generator the state changes to GEN_CLOSED


def is_valid_result(result):
    """
    Validate and return True or False. Do not crash for invalid results
    :param result:
    :return:
    """
    if "experiment_id" in result and "state" in result and "count" in result:
        if isinstance(result["experiment_id"], str) and isinstance(result["state"], str) and isinstance(result["count"], int):
            return True
    return False


def generate_valid_results(results):
    """
    Generates valid dictionaries and discards invalid ones
    :param results: list of result dictionaries
    :return: yield valid results
    """
    for result in results:
        if is_valid_result(result):
            yield result


"""
Reflection: 
1. When does the generator body actually execute?
It is executed upon the first call to the generator, not when it is created. 

2. Why can a generator be useful for large datasets?
When large data sets are processed, it is beneficial to load and process the data in small chunks. Loading the full 
dataset will hog the memory. 
 
3. What happens after the generator is exhausted?
StopIteration is raised. 

4. Why might returning a list be inappropriate here?
To return a list we need to generate all the items, it is an anti-pattern to generator feature. 
"""
