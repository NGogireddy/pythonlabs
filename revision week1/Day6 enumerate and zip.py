# Tracking indices without manual loop counters
gates = ["Hadamard", "CNOT", "Pauli-X"]
for index, gate in enumerate(gates):
    print(f"Gate slot {index}: {gate}")

# Threading data channels together
qubit_labels = ["q0", "q1", "q2"]
frequencies = [4.8, 5.1, 4.9]
for label, freq in zip(qubit_labels, frequencies):
    print(f"Device {label} operates at {freq} Ghz")

# Given a list of competitors in the order they finished a race: runners = ["Alice", "Bob", "Charlie", "David"].
# Use enumerate() inside a list comprehension to generate a list of strings that reads:
# ['1st: Alice', '2nd: Bob', '3rd: Charlie', '4th: David']
runners = ["Alice", "Bob", "Charlie", "David"]
results = [f'{place[0]}{place[1]}: {runner}'
           for place, runner in zip(enumerate(['st', 'nd', 'rd', 'th'], start=1), runners)]
print(results)

#  Merge two matching lists: keys = ["id", "role", "dept"] and values = [101, "Admin", "HR"].
#  Use zip() to instantly merge these into a single dictionary: {"id": 101, "role": "Admin", "dept": "HR"}
keys = ["id", "role", "dept"]
values = [101, "Admin", "HR"]
merged_dict = {key: value for key, value in zip(keys, values)}
print(merged_dict)

# Given a list of values: items = ["a", "b", "c", "d", "e", "f", "g"].
# Use enumerate() and filter() together to keep only the items that sit at even index positions (0, 2, 4, 6),
# returning ['a', 'c', 'e', 'g']
items = ["a", "b", "c", "d", "e", "f", "g"]
filtered_items = [value for index, value in enumerate(items) if index%2 == 0]
print(filtered_items)

# You have a path tracked by two lists of coordinates: x_coords = [1, 4, 9] and y_coords = [2, 6, 14].
# Use zip() to calculate the difference (delta) between consecutive points.
# Specifically, pair the list with a shifted version of itself to find the change in \(x\) and change in \(y\)
# between steps, yielding a list of tuples: [(3, 4), (5, 8)]. (Explanation: 4-1=3, 6-2=4 -> (3,4); 9-4=5, 14-6=8 -> (5,8)
x_coords = [1, 4, 9]
y_coords = [2, 6, 14]
points = list(zip(x_coords, y_coords))
print(points)
# Step 2: Zip points with its own slice to pair up consecutive tuples
# This gives the loop: ((1, 2), (4, 6)) then ((4, 6), (9, 14))
distances = [(p2[0] - p1[0], p2[1] - p1[1]) for p1, p2 in zip(points, points[1:])]
print(distances)

# Given matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. Write a single line of code using zip(), list(),
# and the star unpacking operator * to transpose it into [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(map(list,zip(*matrix))))
