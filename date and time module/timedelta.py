from datetime import datetime

d1 = datetime(2020, 5, 13, 10, 5, 6)
d2 = datetime(2020, 5, 13)

days = d1-d2
print(type(days))
print(days)

print("\\\\")


class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(C, A))

lst = [0, 1, 4, 9, 16]

del lst[lst[1]]

print(lst)

try:
    b = 5/0
except (ValueError, ZeroDivisionError):
    print("First except")
except :
    print("default exception")

a = 1
b = 0
a = a^b
print(a, b)
b = a^b
print(a, b)
a = a^b
print(a, b)

# print(Hello, World!)

lst1 = [i for i in range(1,10)]
print(len(lst1), lst1)
lst2 = lst1[-1:1:-1]
print(len(lst2), lst2)