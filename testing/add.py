def add(a):
    if type(a) not in [list,tuple]:
        raise TypeError("Add() function takes an integer or a float")
    return sum(a)
