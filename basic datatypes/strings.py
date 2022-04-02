print("Program showing the basics of strings")

"""
Sample string used here is 'abcdef'. It has got 6 characters in it. 
In strings indexing starts from 0. 
Fpllowing will be the mapping. 
0 -> a
1 -> b
2 -> c
3 -> d
4 -> e
5 -> f
"""

a = "abcdef"
print(a)
print(type(a))
print("\n")

print("Picking the first character of the string")
print(a[0])
print("\n")

print("Picking the last character of the string when size of string is known")
print(a[5])
print("\n")

print("Picking last character when the size of the string is unknown")
print(a[-1])
print("\n")

print("re-initializing the string with more characters but in single quotes")
a = 'abcdefghij'
print(a)
print(len(a))
print(type(a))

print("Some examples of slicing below")
print(f"Get the first 2 characters of {a}")
print(a[:2])
print("\n")

print(f"3 characters from 4th character of {a}")
print(a[3:6])
print("\n")

print(f"Get the last 2 characters of {a}")
print(a[-2:])
print("\n")

print(f"Reversing the string {a}")
print(a[::-1])
print("\n")

print("Last 3 characters of {} in reverse order".format(a))
print(a[-1:-4:-1])
print("\n")

print("Trying to provide wrong subscripts")
print(a[3:2])
print(a[-3:-1:-1])
print("Nothing gets printed")

