import math

def square(storona):
    if isinstance(storona, int):
        return storona*2
    else: 
        return math.ceil(storona)*2

print(square(4.1))


