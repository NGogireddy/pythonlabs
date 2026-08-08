# Basic inline lambda
add_five = lambda x: x + 5
print(add_five(10))

# Adding 5 to all numbers in the list
numbers = range(1, 11)
revised_numbers = [add_five(number) for number in numbers]
print(revised_numbers)

# Same addition using map
map_numbers = list(map(add_five, numbers))
print(map_numbers)

# lambda function assigned to a variable add_tax that takes a price and returns the total cost after adding 15% tax
add_tax = lambda x: x * 1.15

# lambda function assigned to a variable clean_word that takes a string,
# strips any whitespace from the edges, and converts it entirely to lowercase
clean_word = lambda word: word.strip().lower()

# lambda function to sort this list based on the quantity (the second element) in descending order
inventory = [("apple", 5), ("banana", 2), ("orange", 8)]
inventory.sort(key= lambda item: item[1], reverse=True)
print(inventory)

# Use filter() and a lambda function to extract only the words that are
# longer than 4 characters AND start with the letter 'l' or 'f'.
words = ["lambda", "python", "code", "ai", "function", "exec"]
filtered_words = list(filter(lambda word: len(word) > 4 and word.startswith(('f', 'l')), words))
print(filtered_words)

# lambda function that returns another lambda function. The outer lambda should take a multiplier.
# The inner lambda should take a number and a divisor. If the divisor is 0, it should return 0;
# otherwise, it should divide the number by the divisor and multiply the result by the multiplier
lambda_func = lambda multiplier: lambda number, divisor: 0 if divisor == 0 else multiplier * number/divisor

