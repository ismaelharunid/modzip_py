
try:
  from collections.abc import Iterable
except ImportError:
  from collections import Iterable


class modzip(object):
  
  _index = None
  _count = None
  _max_iterations = None
  _interables = None
  _indexes = None
  _lengths = None
  _cache = None
  
  def __init__(self, *iterables, max_iterations=None):
    indexes = ", ".join("#{:d}".format(i+1) for i in range(len(iterables)) \
        if not isinstance(iterables[i], Iterable))
    if indexes:
      raise TypeError("modzip argument(s) {:s} must support iteration" \
          .format(indexes))
    self._index = 0
    self._count = n = len(iterables)
    self._max_iterations = max_iterations
    self._iterables = tuple(iter(it) for it in iterables)
    self._indexes = list(0 for i in range(n))
    self._lengths = list(None for i in range(n))
    self._cache = tuple([]  for i in range(n))
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self._max_iterations is not None and self._index >= self._max_iterations:
      raise StopIteration('exhausted')
    n = self._count
    iterables = self._iterables
    indexes = self._indexes
    lengths = self._lengths
    cache = self._cache
    result = []
    for i in range(n):
      if lengths[i] is None:
        try:
          value = iterables[i].__next__()
          result.append(value)
          cache[i].append(value)
          indexes[i] += 1
          continue
        except StopIteration:
          lengths[i] = len(cache[i])
          if all(l is not None for l in lengths) and self._max_iterations is None:
            if self._max_iterations is None:
              self._max_iterations = max(self._lengths)
            raise StopIteration('exhausted')
      result.append(cache[i][indexes[i]%lengths[i]])
      indexes[i] += 1
    self._index += 1
    return tuple(result)
  
  def reset(self):
    # make sure we exhausted the iterator or things get out of sync
    if self._max_iterations is None:
      try:
        while True:
          self.__next__()
      except StopIteration:
        self._max_iterations = max(self._lengths)
    self._index = 0
    return self

