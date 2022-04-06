print("All about Tuples here")
print("Tuples are similar to lists except that they are immutable")

t1 = (1,2,3)
print(t1)
# t1[3] = 4
# This will not work as tuples are immutable. Instead we have to reassign t1 like below

t1 = (1,2,3,4)
print(t1)

print('Indexing and slicing works same as lists')
print(t1[0])
print(t1[2:])
print(t1[-1])
print(t1[-2:])

print("!!! Note that after slicing a tuple it returns a tuple not list !!!")
print("\n")

print(f't1.count(5) returns how many times 5 is present: {t1.count(5)}')
print(f'len(t1) returns the number of objects in t1: {len(t1)}')
print(f't1.index(2) returns the index position of 2 in t1: {t1.index(2)}')
print(f't1.index(9) returns ValueError if item is not present in tuples. Similar to lists')
print("\n")

print('Similar to lists the objects inside a tuple need not be of same datatype')
t2 = ('a',[1,2,3],{'a':1,'b':2},(100,200))
print(t2)

t3 = 'a','b','e','n','d','g'
print(type(t3))
print(t3)

t4 = 'c',
print(t4)
t5 = t3 + t4
print(t5)
print("\n")

print("Following functions work if all the objects in the tuple are of same datatype")
print(min(t1))
print(max(t3))
print(sum(t1))
print(sorted(t3))
print(all(t4))
print(any(t3))

