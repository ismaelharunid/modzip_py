# modzip_py
A modulus version of zip that repeats columns until all columns are exhausted

```
class modzip(builtins.object)
 |  modzip(*iterables, max_iterations=None)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, *iterables, max_iterations=None)
 |      Same as zip except it repeats columns until all columns are exhausted.
 |      
 |      Zip with repeating columns until either all columns are exhausted or the
 |      yield count reaches the optional keyword argument "max_iterations".
 |      
 |      iterations (*args):   the iterable columns
 |      max_iterations (int): the number of interations to yield
 |  
 |  __iter__(self)
 |      returns self, no arguments.
 |  
 |  __next__(self)
 |      returns the next set of iterated columns, no arguments.
 |  
 |  reset(self)
 |      Resets the iterables for another run., no arguments.
```

```
>>> from modzip import modzip
>>> mz = modzip(range(10), range(5))
>>> for p in mz:
...   print(p)
... 
(0, 0)
(1, 1)
(2, 2)
(3, 3)
(4, 4)
(5, 0)
(6, 1)
(7, 2)
(8, 3)
(9, 4)
>>> for p in mz:
...   print(p)
... 
>>> mz.reset()
<modzip.modzip object at 0x7f062e048590>
>>> for p in mz:
...   print(p)
... 
(0, 0)
(1, 1)
(2, 2)
(3, 3)
(4, 4)
(5, 0)
(6, 1)
(7, 2)
(8, 3)
(9, 4)
```
