# 2. Set comprehension: Automatic duplicate removal
raw_states = ["up", "down", "up", "unknown", "down"]
unique_states = {state.upper() for state in raw_states}
print(unique_states)

# filter the even numbers from this set of numbers
numbers = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8]
unique_evens = {number for number in numbers if number%2 == 0}
print(unique_evens)

# Create a set of the lengths of all words in a sentence that have more than 3 letters. Ignore duplicates.
text = "python is a very fun and powerful language"
word_lengths = {word_len for word in text.split() if (word_len := len(word)) > 3}
print(word_lengths)

# Extract a unique set of all lowercase vowels found in a list of mixed-case words
words = ["Apple", "Banana", "Cherry", "Date"]
unique_lower_vowels = {letter for word in words for letter in word if letter in ['a', 'e', 'i', 'o', 'u']}
print(unique_lower_vowels)

# Flatten a 2D list of numbers. Keep only numbers that are divisible by 3 and greater than 5
matrix = [[1, 3, 9], [6, 12, 15], [2, 4, 18]]
output = {number for row in matrix for number in row if number>5 and number%3 == 0}
print(output)

# Generate a set of all prime numbers up to a given limit using a single set comprehension
limit = 20
primes = {number for number in range(2, limit+1)
          if (all(number % divisor != 0 for divisor in range(2, int(number**0.5+1))))}
print(primes)
