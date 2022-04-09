print("All you need to know about sets")
print("Sets are un-ordered collection of unique elements")

a = {1,2,3,4,6,7}
b = {'a','b','n','f','h','n'}

print(a)
print(b)
print('Notice that the letter "n" is not stored twice in the set b')

"""
Ways of creating sets
"""
b = set()
# Note: We cannot use {} to create an empty set. This is for dictionaries only

c = set([0,1,4,5,7])
d = set('Mississippi')
print(b)
print(c)
print(d)
print("\n")

print("Some basic operations on sets")
# Add an element to the set
c.add(3)
print(c)
# Remove an element from the set. No exception raised if element is not present
c.discard(3)
c.discard(10)
print(c)
print(f'pop() method removes a random element from the set: {c.pop()}')
print(c)

print("Set operations like Union, intersect, difference")

print("b is an empty set. Intersection of b and c is empty")
print(c.intersection(b))
b1 = {4,5,8,9}

print(f"Set a is  {a}")
print(f"Set b1 is {b1}")
print("Union of a an b should return 1 to 9 in a set")
print(a.union(b1))
print("\n")

print("a intersection b1 should give a set of element 4")
print(a.intersection(b1))
print("\n")

print("Difference of a and b1 should return a set of 1,2,3,6,7")
print(a.difference(b1))
print("\n")

b.add(8)
b.add(9)
print(f"b.issubset(b1) returns true/false: {b.issubset(b1)}")
print(f"b1.issuperset(b) returns true/false: {b1.issuperset(b)}")
print("\n")

print(f"Set a is  {a}")
print(f"Set b is  {b}")
print(f"Both are disjoint sets. isdisjoint() checks for us: {a.isdisjoint(b)}")

print(a.union(b1))
print(a.intersection(b1))
print("Symmetric difference is (A union B) - (A intersection B) or (A-B) union (B-A)")
print(a.symmetric_difference(b1))
print("\n")

print("Making a copy of the set")
copyof_a = a.copy()
print(copyof_a)
print("Popped and element from copy and checking the sets: " + str(copyof_a.pop()))
print(a)
print(copyof_a)
print("\n")

print("Cleared copyof_a")
copyof_a.clear()
print(copyof_a)
copyof_a.add(1)

print("Using update() method")
copyof_a.update(b1)
print(copyof_a)

# intersection will return the set of elements that are present in both the sets
print(copyof_a.intersection(b))

# intersection_update() will update the set with the intersecting elements
copyof_a.intersection_update(b)
print(copyof_a)
print("\n")

# similar to intersection_update we also have symmetric_difference_update and difference_update
print('Here is copy of b1 {}'.format(b1))
print('Here is copy of a  {}'.format(a))
a.symmetric_difference_update(b1)
print('Symmetric diff of a and b1 updated into a is {}'.format(a))

a.difference_update(b1)
print(f'Difference of a and b1 now updated into a is {a}')
print("\n")

print("More about sets can be found in https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset")
