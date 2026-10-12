import copy

"""
## Drill
Predict the result before running each example:

a = [1, 2, 3]
b = a
b.append(4)

Prediction: a = [1, 2, 3, 4], b = [1, 2, 3, 4]

Then compare with:

a = [1, 2, 3]
b = a.copy()
b.append(4)

Prediction: a = [1, 2, 3], b = [1, 2, 3, 4]

Ask:

-   Did `b = a` create a second list?
    No, it did not create a second list. It just assigned the address of the object a to b. Now both a and b points to
    the same list.

-   What does `a is b` tell you?
    When we do b = a then a is b will return True. In the second case it is not.

-   How is `is` different from `==`?
    'is' is True if both the objects refer to the same location. '==' checks if the values in both the objects are same.

"""

a = [1, 2, 3]
b = a
b.append(4)

print(a)
print(b)
print(a is b)
print(id(a))
print(id(b))

c = [1, 2, 3]
d = c.copy()
d.append(4)

print("Results using copy statement.")
print(c)
print(d)
print(c is d)
print(id(c))
print(id(d))

print(c is [1, 2, 3])   # Returns False
print(c == [1, 2, 3])   # Returns True
print([1, 2, 3] is [1, 2, 3])   # Also returns False as each instance of [1, 2, 3] is stored in different location.

print("Working on shallow copy")
original = [[1, 2], [3, 4]]
shallow = original.copy()

# 1. The top-level containers are completely independent
print(original is shallow)  # False (Safe! Different addresses)

# 2. However, the nested items inside them are still aliased!
print(original[0] is shallow[0])  # True (They share the inner lists)

print(id(original))
print(id(shallow))

print(id(original[0]), id(shallow[0]), id(original[1]), id(shallow[1]))
shallow.append([5, 6])
print(id(original[0]), id(shallow[0]), id(original[1]), id(shallow[1]), id(shallow[2]))

try:
    print(id(original[2]))  # Raises index error
except IndexError:
    print("Original is not same object as Shallow. Appending something to shallow will not reflect in original")

print("Working on Deep copy")
orig = [[1, 2], [3, 4]]
deep = copy.deepcopy(orig)  # The top level containers and internal nested items are also copied.

print(orig is deep)
print(id(orig[0]), id(deep[0]), id(orig[1]), id(deep[1]))

# The system sets up a template for a starting shopping cart
DEFAULT_CART = {
    "items": ["laptop", "mouse"],
    "shipping": "free"
}


def checkout_user(username, qualifies_for_gift):
    # 1. Initialize the user's cart using our default template
    user_cart = DEFAULT_CART

    # 2. If they qualify, add their free premium gift
    if qualifies_for_gift:
        user_cart["items"].append("free_premium_headphones")

    print(f"🛒 {username}'s final cart: {user_cart['items']}")


# --- Simulation ---

# User A is a premium member and qualifies for the gift
checkout_user("User_A_Premium", qualifies_for_gift=True)    # Prints laptop, mouse and free_premium_headphones

# User B is a regular member and does NOT qualify for the gift
checkout_user("User_B_Regular", qualifies_for_gift=False)   # Prints laptop, mouse and free_premium_headphones

# Once the user A checkout is done it modified the DEFAULT_CART and the same is used for user B.


# The system sets up a template for a starting shopping cart
DEFAULT_CART1 = {
    "items": ["laptop", "mouse"],
    "shipping": "free"
}


def fixed_checkout_user(username, qualifies_for_gift):
    # 1. Initialize the user's cart using our default template
    user_cart = copy.deepcopy(DEFAULT_CART1)

    # 2. If they qualify, add their free premium gift
    if qualifies_for_gift:
        user_cart["items"].append("free_premium_headphones")

    print(f"🛒 {username}'s final cart: {user_cart['items']}")


# User C is a premium member and qualifies for the gift
fixed_checkout_user("User_C_Premium", qualifies_for_gift=True)    # Prints laptop, mouse and free_premium_headphones

# User D is a regular member and does NOT qualify for the gift
fixed_checkout_user("User_D_Regular", qualifies_for_gift=False)   # Prints laptop, mouse


def remove_sensitive_data(user_profile):
    # The function argument 'user_profile' becomes an alias
    # to whatever dictionary is passed into it.

    # ❌ This mutates the original object in place!
    del user_profile["password_hash"]
    del user_profile["social_security_number"]

    user_profile["status"] = "Cleaned"
    return user_profile


# --- The Bug in Action ---

original_profile = {
    "name": "Alice",
    "password_hash": "a8f9c2...",
    "social_security_number": "000-12-3456",
    "status": "Raw"
}

# You pass the dictionary to the cleaner function
cleaned = remove_sensitive_data(original_profile)

# Later in the code, you try to log the original raw data...
print("Original Profile SSN:", original_profile.get("social_security_number"))  # Output: Original Profile SSN: None
print(f"Original profile is: {original_profile}, address is {id(original_profile)}")
print(f"Cleaned profile is: {cleaned}, address is {id(cleaned)}")

# Pro-tip, never pass directories as parameters to the function as any modifications in the function will be reflecting
# on the original variable.


def add_sum_to_list(input_list):
    """
    a small function that accepts a list and returns a list with sum of values as a result list.
    It will not modify the caller's list.
    :param input_list:
    :return: list
    """
    output = copy.deepcopy(input_list)
    output.append(sum(input_list))
    return output


"""
> Why can two variables refer to the same mutable object, and what bug could that create in a larger application?
When assignment is done for mutable objects like list, dict, set the id of the original object is shared with the 
target variable, so any changes on the original or target will be reflected in both the references and could create 
major issues. 
"""
