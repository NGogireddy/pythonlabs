# Given a list of temperatures in Fahrenheit: f_temps = [32, 68, 104, 212]. Use map() to convert them all to Celsius
# Formula: (F - 32) * 5/9
f_temps = [32, 68, 104, 212]
c_temps = list(map(lambda x: (x - 32) * 5/9, f_temps))
print(c_temps)

# Given a list of words: words = ["apple", "banana", "kiwi", "sky"]. Use map() to return
# a list of integers representing the count of vowels (a, e, i, o, u) in each word
words = ["apple", "banana", "kiwi", "sky"]
vowel_count = list(map(lambda word: sum(1 for letter in word if letter.lower() in r'aeiou'), words))
print(vowel_count)

# You have two lists of numbers of equal length: list_a = [1, 2, 3, 4] and list_b = [10, 20, 30, 40].
# Use map() to multiply the numbers at corresponding indexes together to get [10, 40, 90, 160]
list_a = [1, 2, 3, 4]
list_b = [10, 20, 30, 40]
product_list = list(map(lambda x, y: x * y, list_a, list_b))
print(product_list)

# Use map() to return a new list of dictionaries where the email values are replaced with "HIDDEN",
# but the names remain untouched.
users = [{"name": "Alice", "email": "alice@email.com"}, {"name": "Bob", "email": "bob@email.com"}]
masked_users = list(map(lambda user: {"name": user["name"], "email": "HIDDEN" }, users))
print(masked_users)
# use the dictionary union operator (|) to merge or overwrite keys on the fly like this
# works on Python 3.9+
# list(map(lambda user: user | {"email": "HIDDEN"}, users))


# Given a 2D list (a matrix) representing rows: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# Use map() alongside a lambda function to transpose it into columns: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[matrix[col][row] for col in range(len(matrix))] for row in range(len(matrix[0]))]
transpose1 = list(map(lambda *rows: list(rows), *matrix))
transpose2 = list(map(lambda col: [row[i] for row in matrix], range(len(matrix[0]))))
print(transpose1)
print(transpose2)