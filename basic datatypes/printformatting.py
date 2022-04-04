print("Different ways of printing in python is illustrated here")

print("using .format() method")
print("\n")

name = 'James'
middle_name = 'Hunt'
print("My name is {} and my middle name is {}".format(name,middle_name))
print("The same can also be achieved by providing index positions in the braces. See below command")
print("\n")
print("My name is {1} and my middle name is {0}".format(middle_name,name))
print("This however might be slightly confusing. We can add clarity by assigning variable names like here")
print("\n")
print("My name is {n} and my middle name is {m}".format(n=name,m=middle_name))
print("\n")

print("Printing floating point numbers with precision")
print("Following will be useful while printing accounts")

cost = 100
items = 3
cost_per_item = cost/items

print("Cost of items {c}. Cost per item is {cp}".format(c=cost,cp=cost_per_item))
print("\n")
print("Rounding the cost to 2 digits after decimal")
print("Cost of items {c}. Cost per item is {cp:1.2f}".format(c=cost,cp=cost_per_item))
"""
in the above command cp:1.2f 1 stands for the width and 2 stands for the number of precision
the value in width matters when you want to align the cost to the right side. Examples given below
"""

mangoes_cost = 150.56
apples_cost  = 10.00
plums_cost   = 5.626

print("Mangoes {m:6.2f}".format(m=mangoes_cost))
print("Apples  {a:6.2f}".format(a=apples_cost))
print("Plums   {a:6.2f}".format(a=plums_cost))
print("Total   {a:6.2f}".format(a=mangoes_cost+apples_cost+plums_cost))

"""
Increasing the width to 10 to see how it works
"""
print("\nIncreased the width to 10 from 6. Output below")
print("Mangoes {m:10.2f}".format(m=mangoes_cost))
print("Apples  {a:10.2f}".format(a=apples_cost))
print("Plums   {a:10.2f}".format(a=plums_cost))
print("Total   {a:010.2f}".format(a=mangoes_cost+apples_cost+plums_cost))

"""
Decreasing the width to 3 to see how it works
"""
print("\nDecreased the width to 3 from 10. Output below")
print("Mangoes {m:3.2f}".format(m=mangoes_cost))
print("Apples  {a:3.2f}".format(a=apples_cost))
print("Plums   {a:3.2f}".format(a=plums_cost))
print("Total   {a:3.2f}".format(a=mangoes_cost+apples_cost+plums_cost))

"""
Decreasing the precision to 1 to see how it works
"""
print("\nDecreased the precision to 1 from 2. Width is reset to 6. Output below")
print("Mangoes {m:6.1f}".format(m=mangoes_cost))
print("Apples  {a:6.1f}".format(a=apples_cost))
print("Plums   {a:6.1f}".format(a=plums_cost))
print("Total   {a:6.1f}".format(a=mangoes_cost+apples_cost+plums_cost))

"""
Width will add white space to the output we are printing if our variable is smaller than the width specified. 
precision is to tell how many digits we want after the decimal
"""

print("More detailed information about print formatting is available in :")
print("https://pyformat.info")

print("using F-string method")
print("\n")

print(f"My name is {name} and my middle name is {middle_name}")
"""
Changed cost of plums to -ve
"""
plums_cost = -6.078

print(f"Mangoes   {mangoes_cost:6.2f}")
print(f"Apples    {apples_cost:6.2f}")
print(f"Plums     {plums_cost:6.2f}")

"""
Use '0' before the format specification to left pad with 0's 
"""

print(f"Mangoes   {mangoes_cost:010.2f}")
print(f"Apples    {apples_cost:010.2f}")
print(f"Plums     {plums_cost:010.2f}")

"""
Use '=' before the format specification to display the - sign at the start of the print 
"""

print(f"Mangoes   {mangoes_cost:=10.2f}")
print(f"Apples    {apples_cost:=10.2f}")
print(f"Plums     {plums_cost:=10.2f}")

"""
Use '<^>>' before the format specification to align the text to the left/centre/right 
"""
print(f"Mangoes   {mangoes_cost:_^10.2f}")
print(f"Apples    {apples_cost:_^10.2f}")
print(f"Plums     {plums_cost:_^10.2f}")

print(f"Mangoes   {mangoes_cost: <10.2f}")
print(f"Apples    {apples_cost: <10.2f}")
print(f"Plums     {plums_cost: <10.2f}")

