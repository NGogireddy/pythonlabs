import matplotlib.pyplot as plt
import numpy as np
import random


"""
## Drill
Before using Matplotlib, answer:

1.  What does the x-axis represent?
It represents the dimension of the graph, eg age, time, department, etc

2.  What does the y-axis represent?
It can represent the value of the dimension. eg salary, speed, count etc

3.  What does one point `(x, y)` represent?
A point is used to represent the property of the subject eg at this time this is the speed/distance. 

4.  What happens if `x` and `y` have different lengths?
X and Y can have different lengths as the values represented on Y can be anything e.g height of a person with respect to 
age will be limited range, but salary corresponding to age can have a broad range. 

5.  What does a line connecting points communicate that individual points do not?
A line will show the trend which is not visible just with the presentation of individual points. 

"""


def basic_plot():
    arr = np.array([0, 2, 3, 5, 6])
    plt.plot(arr, color='red', linestyle='--', linewidth=2.5, marker='^', label="Team 'A' Score")
    plt.xlabel('Time')
    plt.ylabel('Points')
    plt.title('Progress')
    plt.legend()
    plt.xlim(0, 5)
    plt.ylim(0, 7)
    plt.grid()
    plt.show()


def logarthamic_plot():
    x = [1, 2, 3, 4, 5]
    y = [10, 100, 1000, 10000, 100000]

    # 1. Plotting with line style, color, marker, and label parameters
    plt.plot(x, y, color='purple', linestyle='--', linewidth=2, marker='o', label='Growth Rate')

    # 2. Applying scale and limit parameters
    plt.yscale('log')  # Uses a logarithmic scale due to exponential Y values
    plt.xlim(1, 5)

    # 3. Label parameters
    plt.xlabel('Timeline (Days)')
    plt.ylabel('Value (Log Scale)')
    plt.title('Projected Experimental Results')
    plt.legend()  # Enables the 'Growth Rate' label visibility

    plt.show()


def basic_scatter():
    arr = np.array([random.random() for _ in range(500)])
    plt.scatter(range(500), arr, label='Simulation')
    plt.xlabel('Experiment Number')
    plt.ylabel('Probability result')
    plt.legend()
    plt.show()


def give_compounding_returns(investment=1000, timeperiod=10, roi=9.0):
    """
    Takes the initial investments and returns a numpy 2d array having [time, amount] for each year
    :param investment: Positive Integer
    :param timeperiod: Positive Integer from 1 to 50
    :param roi: Positive float from 0 to 25
    :return: numpy 2d array
    """
    if investment > 0 and 0 < timeperiod <= 50 and 0 < roi <= 25:
        years = np.arange(0, timeperiod + 1)
        amounts = investment * ((1 + roi / 100) ** years)
        return np.column_stack((years, amounts))
    return np.empty((0, 2))


def plot_compounding_returns(arr):
    """
    Takes a 2d array of time and amount and plots it.
    :param arr:
    :return: None
    """
    if isinstance(arr, np.ndarray) and arr.ndim == 2 and arr.dtype.kind in 'iuf' and arr.size > 0:
        plt.plot(arr[:, 0], arr[:, 1], label='Investment Returns')
        plt.xlabel('Time in years')
        plt.ylabel('Returns')
        plt.legend()
        plt.grid()
        plt.show()

"""
Reflection: 
I have voluntarily skipped testing give_compounding_returns as it is not related to matplotlib and todays concepts are
new to me which is already taking time, however I got a basic Idea on how plotting works on 1d and 2d array inputs.

> What information became easier to understand visually than from inspecting the NumPy array?
Visually looking the data points is easier than looking at numbers, especially when the sample size is huge. Numbers 
wouldn't give us the story better. It would be hard to deduce the story looking at the raw values.  

"""