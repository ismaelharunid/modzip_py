# modzip_py
A modulus version of zip that repeats columns until all columns are exhausted


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
