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

print('Slicing in steps. a[::2] will print the alternate characters')
print(a[::2])
print("\n")

print('Slicing in steps. a[::3] will print the third character skipping 2')
print(a[::3])
print("\n")

print("This is very powerful, we can use it in combination with range. Ex, a[3:9:2]")
print(a[3:9])
print(a[3:9:2])
print("\n")

print("Strings are immutable i.e, we cannot change values at specific position")
print("Following wouldn't work a[0] = 'z'. Uncomment and check for yourself ")
# a[0] = 'z'
print(a)
print('\n')

print("Instead total re-assigning works. i.e, a = 'xyz' will completely change the value in a")
a='xyz'
print(a)
print("\n")

print("Concatenating two strings is just like adding two numbers")
b = 'pqr'
c = a + b
print(f"{a} + {b} = {c}")
print("\n")

print("You can multiply a string with number. See what happens")
c = b * 3
print(f"{b} * 3 = {c}")
print('\n')

print('Strings has got multiple inbuilt methods. Here are some examples')
a = 'XyZ'
print(f"a is {a}")
print(f"a.find('y') returns {a.find('y')}")
print(f"a.find('z') returns {a.find('z')}. 'z' is not same as 'Z'")
print(f"a.endswith('Z') returns {a.endswith('Z')}. Checks if a ends in 'Z'")
print(f"a.join('aBc') returns {a.join('aBc')}. Here 'aBc' is joined with 'XyZ' ie aBc individual letters")
print(f"a.count('x') returns number of occurances of 'x' in a:  {a.count('x')}")
print(f"a.find('X') returns index of first occurance of 'X' or -1 if not found: {a.find('X')}")
print(f"a.find('Y') returns index of first occurance of 'Y' or -1 if not found: {a.find('Y')}")
print(f"a.capitalize() returns {a.capitalize()}")
print(f"a.center(20,'*') returns {a.center(20,'*')}. Fits the string inbetween 17 (20-len(a)) '*' ")
print(f"a.casefold() turns it into {a.casefold()}")
print(f"'mNoP'.swapcase() returns a string of characters with reverse casing : {'mNoP'.swapcase()}")
print("\n")

print("Encoding a string. returns a bytes literal of the passed text")
txt = "My ±#name is Ståle"
print(txt.encode("ascii","ignore"))
print(type(txt.encode("ascii","ignore")))
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
print("For possible encodings, errors and their codes refer link below")
# https://docs.python.org/3/library/codecs.html#standard-encodings
# https://docs.python.org/3/library/codecs.html#codecs.register_error
print("\n")

tab_raw = r'ab\tabc\tabcd\tabcde\tabcdef\tabcdefg'
tab = 'ab\tabc\tabcd\tabcde\tabcdef\tabcdefg'
print(f"Here is a string with escape characters in it:  {tab_raw}")
print(f"tab.expandtabs(7) returns {tab.expandtabs(7)}")
print("Play around with the number passed as parameter to understand how it works")
print("\n")

a = 'abcdefghij'
print(f"String stored in a is {a}")
print(f"a.index('e') returns the index of 'e' in the string a {a.index('e')}")
print("Note: If e is not present in the string it throws error.")
print("\t You can also pass start and end range subscripts after the search string")
print(f"For eg a.index('d',1,7) returns {a.index('d',1,7)}")
print("\n")

print("Following are functions to check the strings")
print(f"'Hellow123'.isalnum() checks if the string is alpha numberic: {'Hellow123'.isalnum()}")
print(f"'Hellow123'.isalpha() checks if the string is alphabetic: {'Hellow123'.isalpha()}")
print(f"'Hellow123'.isascii() checks if the string has ascii values only: {'Hellow123'.isascii()}")
print(f"'123'.isdigit() checks if the string has numerals only: {'123'.isdigit()}")
print(f"'Hellow123'.islower() checks if the string is in lower case: {'Hellow123'.islower()}")
print(f"'123.321'.isdecimal() checks if the string has numerals only: {'123.321'.isdecimal()}")
print(f"'e2155'.isnumeric() checks if the string has numerals only: {'e2155'.isnumeric()}")
print(f"'elif'.isidentifier() checks if the string 'if' is a keyword: {'elif'.isidentifier()}")
print(f"'{txt}'.isprintable() checks if the string is printable: {txt.isprintable()}")
print(f"'  '.isspace() checks if the string is empty : {'  '.isspace()}")
print(f"'Bbc News'.istitle() checks if the string is in Title format (Camel case) : {'Bbc News'.istitle()}")
print(f"a.isupper() checks if all the strings are in uppercase : {a.isupper()}")
print("\n")

print("More documentation can be found in: ")
print("https://docs.python.org/3/library/stdtypes.html#string-methods")
