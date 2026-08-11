from functools import reduce
# filter applies the function on the iterable and returns a collection
nums = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, nums))
print(even_numbers)

# reduce applies the function to the arguments and repeats for all the iterables in it.
sum_nums = reduce(lambda x, y: x + y, nums)
print(sum_nums)

# Given a list of strings containing mixed data and empty entries: data = ["Python", "", "Java", " ", "C#", None, "Go"].
# Use filter() to remove all empty strings, strings that are just spaces, and None values.
data = ["Python", "", "Java", " ", "C#", None, "Go"]
filtered_data = list(filter(lambda x: x and x.strip(), data))
print(filtered_data)

# Given a list of words: words = ["Functional", "Programming", "With", "Python"]. Use reduce() to join these words
# together into a single sentence separated by hyphens (e.g., "Functional-Programming-With-Python").
words = ["Functional", "Programming", "With", "Python"]
joined_word = reduce(lambda x, y: x + '-' + y, words)
print(joined_word)

# Given a list of integers: numbers = [23, 89, 45, 12, 78, 92, 56].
# Use reduce() and a lambda function to find the maximum number in the list.
numbers = [23, 89, 45, 12, 78, 92, 56]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)

# Given a list of numbers: scores = [12, 45, 60, 23, 88, 30, 95].
# In a single line of code, use filter() to keep only the numbers greater than or equal to 50,
# and then use reduce() to calculate the sum of those filtered numbers
scores = [12, 45, 60, 23, 88, 30, 95]
sum_big_numbers = reduce(lambda x, y: x + y, list(filter(lambda x: x >= 50, scores)))
print(sum_big_numbers)

# Given a list of dictionaries representing log entries, where each dictionary has a single key-value pair
logs = [{"status": "200"}, {"user": "Alice"}, {"action": "login"}]
simplified_log = reduce(lambda x, y: x | y, logs, {})
print(simplified_log)
