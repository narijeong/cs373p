#!/usr/bin/env python3

# ------------
# Iterators.py
# ------------

# https://docs.python.org/3.5/library/stdtypes.html#iterator-types

import types

class A :
    class B :
        def __init__ (self) :
            self.i = 2

        def __iter__ (self) :
            return self

        def __next__ (self) :
            if self.i == 5 :
                raise StopIteration
            j = self.i
            self.i += 1
            return j

    def __iter__ (self) :
        return A.B()

print("Iterators.py")

x = A()
assert type(x) is A
assert not hasattr(x, "__next__")
assert     hasattr(x, "__iter__")
assert(list(x) == [2, 3, 4])
assert(list(x) == [2, 3, 4])

p = iter(x)
assert type(p) is A.B
assert hasattr(p, "__next__")
assert hasattr(p, "__iter__")
assert(list(p) == [2, 3, 4])
assert(list(p) == [])

p = iter(x)
assert next(p) == 2
assert next(p) == 3
assert next(p) == 4

try :
    assert next(p) == 5
    assert False
except StopIteration as e :
    assert type(e)      is StopIteration
    assert type(e.args) is tuple
    assert len(e.args)  == 0
else :
    assert False

q = iter(p)
assert q is p

print("Done.")
