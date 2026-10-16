import timeit
import tracemalloc

"""
Learn the basics of:

-   `timeit`
    A module designed specifically for timing small code snippets.

-   repeatable comparisons
    It is finding out the best possible run time of a module by repeating the tests and comparing it with another module
    that returns the same outcome.

-   warm-up/noise and why one timing is weak evidence
    There are multiple reasons why running the job once and taking the evidence is not ideal.
        1. The first run is always slow as the cache needs to be built to load the instructions.
        2. Os might need to fetch data from disk and load it into RAM.
        3. Python might need to initial lookups or optimizations.
        4. More over the run time is impacted by the other background tasks running in the computer which also share RAM

-   `time.perf_counter()` for simple elapsed-time measurements
    returns the absolute value (in fractional seconds) of a high-resolution performance counter provided by the OS.

-   `tracemalloc` for Python allocation investigations, with the caveat that it does not capture every NumPy/native
     allocation in the same way

     While time measures speed, tracemalloc is Python’s built-in tool for measuring memory allocations. It takes
     snapshots of Python's internal memory manager to show you exactly which line of code allocated the most RAM.
     tracemalloc relies entirely on tracking memory handled directly by the CPython interpreter.
     it cannot accurately track memory allocated inside compiled C/C++ or Fortran extensions
     (like NumPy, Pandas, or heavy Machine Learning libraries).

"""


def sum_squares_list_comprehension(numlist):
    """
    Returns the sum of squares of all the numbers in the list.
    :param numlist:
    :return:
    """
    squares = [num**2 for num in numlist]
    return sum(squares)


def sum_squares_lazy_processing(numlist):
    return sum(num**2 for num in numlist)


# Generate a clean dataset of 50,000 integers
test_data = list(range(50_000))


# --- MEMORY TESTING (tracemalloc) ---
def profile_memory(func, data):
    tracemalloc.start()
    func(data)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak / 1024  # Convert to Kilobytes (KB)


mem_list = profile_memory(sum_squares_list_comprehension, test_data)
mem_gen = profile_memory(sum_squares_lazy_processing, test_data)

# --- TIME TESTING (timeit) ---
# We use lambda functions to cleanly pass our data without global lookup overhead
# We repeat the test 5 times, running 50 iterations each, to establish repeatable evidence
runs_list = timeit.repeat(lambda: sum_squares_list_comprehension(test_data), repeat=10, number=50)
runs_gen = timeit.repeat(lambda: sum_squares_lazy_processing(test_data), repeat=10, number=50)

# The Golden Rule: Use min() to ignore operating system noise spikes
min_time_list = min(runs_list)
min_time_gen = min(runs_gen)
max_time_list = max(runs_list)
max_time_gen = max(runs_gen)
avg_time_list = sum(runs_list)/10
avg_time_gen = sum(runs_gen)/10


# --- DISPLAY RESULTS ---
print(f"{'Metric':<25} | {'List Comprehension':<20} | {'Generator Expression':<20}")
print("-" * 73)
print(f"{'Peak Memory Allocation':<25} | {mem_list:>17.2f} KB | {mem_gen:>17.2f} KB")
print(f"{'Min Execution Time':<25} | {min_time_list:>17.4f} s  | {min_time_gen:>17.4f} s")
print(f"{'Max Execution Time':<25} | {max_time_list:>17.4f} s  | {max_time_gen:>17.4f} s")
print(f"{'Avg Execution Time':<25} | {avg_time_list:>17.4f} s  | {avg_time_gen:>17.4f} s")

"""
> What evidence would you need before claiming one implementation is better?
We need to ensure that there is no noise, so we need to repeat the experiment multiple times and take the best run time
from the results.  
"""
