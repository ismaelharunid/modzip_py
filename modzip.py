
try:
  from collections.abc import Iterable
except ImportError:
  from collections import Iterable


class modzip(object):
    
  _index = None
  _count = None
  _max_iterations = None
  _columns = None
  
  def __init__(self, *iterables, max_iterations=None):
    indexes = ", ".join("#{:d}".format(i+1) for i in range(len(iterables)) \
        if not isinstance(iterables[i], Iterable))
    if indexes:
      raise TypeError("modzip argument(s) {:s} must support iteration" \
          .format(indexes))
    self._index = 0
    self._count = n = len(iterables)
    self._max_iterations = max_iterations
    self._columns = tuple([iter(iterables[i]), [], None] for i in range(n))
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self._max_iterations is not None and self._index >= self._max_iterations:
      raise StopIteration('exhausted')
    n = self._count
    result = []
    for i in range(n):
      iterable, cache, length = self._columns[i]
      if length is None:
        try:
          value = iterable.__next__()
          result.append(value)
          self._columns[i][1].append(value)
          continue
        except StopIteration:
          self._columns[i][2] = length = len(cache)
          if all(column[2] is not None for column in self._columns) \
              and self._max_iterations is None:
            self._max_iterations = max(column[2] for column in self._columns)
            raise StopIteration('exhausted')
      result.append(cache[self._index%length])
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
