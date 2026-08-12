# ============================================================
# WEEK 1 CAPSTONE: THE QUANTUM DATA PREPROCESSOR
# ============================================================
# Scenario: You have raw state values from a simulated quantum
# sensor. The dataset contains valid floats, negative numbers,
# and corrupted 'None' values.
#
# Your Tasks:
# 1. Filter out all 'None' values and negative numbers using
#    a single list comprehension.
# 2. Pass that filtered list to a native map() function with a
#    lambda to square each number (simulating an amplitude probability).
# 3. Use enumerate() to loop over the final results and print
#    each value paired with its final index in a clean string format.
# ============================================================

raw_data = [0.5, -0.2, None, 0.9, 1.2, None, -0.8]

cleansed_data = [x for x in raw_data if x and x >= 0]
amplitude_probability = list(map(lambda x: x**2, cleansed_data))
for index, value in enumerate(amplitude_probability, start=1):
    print(f"{index}: {value}")