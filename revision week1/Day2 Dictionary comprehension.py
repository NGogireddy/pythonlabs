# 1. Dictionary comprehension: Mapping IDs to status
qubit_ids = [0, 1, 2, 3, 4]
qubit_map = {f"q{i}": "initialized" for i in qubit_ids}
print(qubit_map)

# Convert a list of words into a dictionary where the word is the key and its length is the value
fruits = ["apple", "banana", "cherries"]
fruit_count = {item: len(item) for item in fruits}
print(fruit_count)

# Take an existing dictionary of items and prices. Increase all prices by 10%,
# but only include items in the new dictionary if their original price was greater than £5.00
item_prices = {"milk": 1.20, "bread": 1.50, "cheese": 6.00, "coffee": 8.00}
filtered_item_prices = {item: price * 1.1 for item, price in item_prices.items() if price > 5.00}
print(filtered_item_prices)

# Merge two parallel lists—one containing employee usernames and the other containing their unique ID numbers
# —into a single lookup dictionary
usernames = ["alpha_dev", "beta_tester", "gamma_mgr"]
ids = [101, 102, 103]
employee_ids = {name:id for name, id in zip(usernames,ids)}
print(employee_ids)

# Build a dictionary from a list of products. If an item's stock is 0, its value should be "Out of Stock".
# If its stock is greater than 0, its value should be "In Stock"
stock_list = [("Laptop", 5), ("Mouse", 0), ("Monitor", 2), ("Keyboard", 0)]
stock_status = {item: "In Stock" if count > 0 else "Out of Stock" for item, count in stock_list}
print(stock_status)

# Simulate parsing raw JSON data from an API response. You have a list of user profile dictionaries.
# Create a single flat lookup dictionary where the key is the user's username and the value is their nested city
api_data = [
    {"id": 1, "username": "alice99", "location": {"city": "London", "country": "UK"}},
    {"id": 2, "username": "bob_codes", "location": {"city": "New York", "country": "US"}},
    {"id": 3, "username": "charlie_dev", "location": {"city": "Tokyo", "country": "JP"}}
]
user_cities = {entry["username"]: entry["location"]["city"] for entry in api_data}
print(user_cities)