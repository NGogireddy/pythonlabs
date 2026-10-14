import gc
import sys

"""
## Drill

values = [1, 2, 3]
alias = values
del values

Prediction: We cannot refer to the list [1, 2, 3] using values but alias still points to the list [1, 2, 3]
"""

values = ['abc', 'def']
alias = values
print(id(values))
print(id(alias))
del values
print(alias)
print(id(alias))
try:
    print(id(values))
except NameError:
    print(f'Values is not available now it is deleted')

"""
-   Has the list necessarily been destroyed?
    No the list is not deleted.  

-   Does `alias` still refer to it?
    Yes, it does. 
    
-   What does `del` actually remove?
    It is the reference to the variable values is deleted.

"""

"""
## Learn 

-   references and object lifetime
    When an object is created and assigned to a variable the address of the object is assigned to the variable in the 
    namespace. When a new reference is added to that object and If the original variable is deleted the object is still 
    available as there is another reference to it. If the second reference is also deleted then the object is completely
    delete. 
     
-   reference counting as a CPython implementation detail
    In the above example when values is defined and assigned to [1, 2, 3] the object [1, 2, 3] is created in the memory
    and reference to that is assigned to values. The number of references to the object is set to 1. When alias is also
    assigned the same reference using alias = values, the reference count to the object increases to 2 as both variables
    are now pointing to [1, 2, 3]. The moment variables are deleted from the namespace the counters are decremented. 
    When the reference count reaches zero, the object is deleted. 
    
-   cyclic garbage collection
    When there are cyclic references in two variables eg: a = [] and b = [], a.append(b), b.append(a). There are cyclic 
    references to a and b. del a and del b will remove the access to the variables but the garbage collector does not 
    have access to delete them as the reference count is 1 for a and b. Cyclic Garbage Collector (GC) ignores reference 
    counts from outside the cycle. It temporarily subtracts internal references within a group of isolated objects. If 
    an object's reference count drops to 0 during this trial subtraction, the GC knows the object is only kept alive by 
    a loop. 
     
-   why `del` removes a name/reference rather than guaranteeing immediate destruction
    del statement only deletes the reference from namespace, if the original object is deleted then any alias variables 
    will loose access to the object, causing the programs to fail. 
    
-   why explicit resource management (`with`) is different from garbage collection. 
    garbage collection runs at regular intervals, with files, dblocks and network sockets it is best practice to release
    the resources as soon as the need is done. Leaving it to GC will hold the resources for a longer time and may lead 
    to resource exhaustion. 
"""


# 1. Create a list object.
# The variable 'a' holds 1 reference to it.
a = [1, 2, 3]
print(f"Initial count: {sys.getrefcount(a)}")  # Prints 2 (1 actual + 1 temporary)

# 2. Add a second reference
b = a
print(f"After b = a: {sys.getrefcount(a)}")     # Prints 3 (2 actual + 1 temporary)

# 3. Pass it into a container (list)
c = [a]
print(f"After putting in a list: {sys.getrefcount(a)}")  # Prints 4 (3 actual + 1 temporary)

# 4. Remove references
del c
del b
print(f"After deleting b and c: {sys.getrefcount(a)}")   # Drops back to 2 (1 actual + 1 temporary)

"""
sys.getrefcount() creates a temporary reference when you pass an object to it, the returned count will always 
be 1 higher than the actual references
"""


# Ensure the GC is turned on, then clear any existing garbage
gc.enable()
gc.collect()


# 1. Setup the cyclic reference
p = []
q = []

p.append(q)
q.append(p)

# Check the reference count (1 for the variable name, 1 for the partner link + 1 temporary)
print(f"p ref count: {sys.getrefcount(p)}")

# 2. Break the main references to isolate the cycle
del p
del q

# At this point, the variables are unreachable by our script, but still exist in memory!
print(f"Is GC tracking the isolated cycle? {gc.isenabled()}")

# 3. Force the cyclic garbage collector to run
# gc.collect() returns the number of unreachable objects it found and cleared
unreachable_count = gc.collect()
print(f"GC successfully collected {unreachable_count} objects.")  # Will show a number > 0

"""
> Why is "I deleted the variable" not the same statement as "the object has definitely been destroyed"?
Deleting the variable will just remove the variable name from the namespace. The object still remains in the memory. 
When all the references to the object are deleted then the object is completely destroyed. 
"""
