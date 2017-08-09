import functools

def int2(x,base=2):
    return int(x,base)

int2 = functools.partial(int,base=2)

print int2('1000000')

print int2('1010101')

