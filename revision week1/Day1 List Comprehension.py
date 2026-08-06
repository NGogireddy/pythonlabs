# Basic list comprehensions
squares = [x ** 2 for x in range(10)]
print(squares)

# Filtering using list comprehension
even_squares = [x for x in squares if x % 2 == 0]
print(even_squares)

# Filter and transform in one line
stripped_list = [str(x).strip() for x in ["alpha ", "beta\n", " gamma\nc", "etc"] if "a" in x]
print(stripped_list)

# Given `prices = [120, 85, 200, 45, 150]`. Write a single-line list comprehension that applies a 10% discount
# but *only* to items that cost more than 100.
prices = [120, 85, 200, 45, 150]
final_price = [x*0.9 if x>100 else x for x in prices ]
print(final_price)

# Create a list that multiplies even numbers by 2 and odd numbers by 3.
numbers = range(1,6)
output_numbers = [x*2 if x%2 == 0 else x*3 for x in numbers]
print(output_numbers)

# Strip trailing spaces from names and filter out any usernames that are shorter than 4 characters after stripping
names = ["alex ", "bob ", "charlie", " joe", "david"]
long_names = [stripped_name for x in names if len(stripped_name := str(x).rstrip())>3]
print(long_names)

# Flatten a 2D matrix (a list of lists) into a single 1D list.
matrix = [[1, 2], [3, 4], [5, 6]]
flat_matrix = [y for x in matrix for y in x]
print(flat_matrix)

# Convert numerical scores into letter grades based on three tiers:
# 90 and above is "A", 70 to 89 is "B", and anything below 70 is "F"
scores = [95, 65, 82, 90, 45]
score_grades = ['A' if x > 89 else 'B' if x > 69 else 'F' for x in scores]
print(score_grades)

# Swap the rows and columns of a matrix using a nested list comprehension
# (turning a 2x3 matrix into a 3x2 matrix)
grid = [[1, 2, 3], [4, 5, 6]]
transpose_grid = []
for x in range(len(grid[0])):
    new_row = []

    for y in range(len(grid)):
        new_row.append(grid[y][x])

    transpose_grid.append(new_row)

print(transpose_grid)

comp_grid = [[grid[y][x] for y in range(len(grid))] for x in range(len(grid[0])) ]

print(comp_grid)