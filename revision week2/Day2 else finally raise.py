# Muscle memory practice
try:
    # logic that can fail
    percent = 20/10*100
except ZeroDivisionError:
    # handle the zero division error
    print("Division by zero is not possible")
else:
    # logic if exception is not raised
    print(f"Percentage is {percent}")
finally:
    print("finally executes in all cases error raised or not")


# challenge 1
def process_reading(value):
    """
    :param value: input to convert into float
    :return: convert to float, validate, square it and return.
    """
    squared_v = 0
    try:
        float_v = float(value)
    except ValueError:
        print(f"Cannot convert {value} to a float number")
    else:
        if 0 < float_v <= 1:
            squared_v = float_v ** 2
        else:
            print(f"{float_v} is not in the limits")
    finally:
        return squared_v


print(process_reading("abd"))


# challenge 2
def process_reading_2(value):
    """
    :param value: floating input to process 
    :return: squared value if it is in the limits
    :raises: ValueError if it is out of bounds
    """
    squared = 0
    try:
        number = float(value)
    except ValueError:
        print(f"{value} is not numeric")
    else:
        if number < 0 :
            raise ValueError("Input cannot be negative")
        elif number > 1 :
            raise ValueError("Input should be between 0 and 1")
        else :
            squared = number**2
    return squared


try:
    result = process_reading_2(0.4)
except ValueError:
    print("Caught ValueError")
else:
    print(f"{result} is returned")

# Why is try except else better than having everything in try block.
"""
try block should be used to execute code that could fail so that we can catch the failures and handle the failures in 
except block for the program to gracefully exit or continue. Else block can be used if no problems arise i.e, all is 
well. Writing everything in try block would be detrimental for the maintenance and readability of the code. 

Also remember that we can raise our own Errors for business validation failures and handle them in our function or pass 
it back to the calling module to handle it there. 
PS: If you are raising an Error then do no have finally if you are returning the error to the calling module.   
"""