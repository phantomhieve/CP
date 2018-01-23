from math import ceil
from sys import stdout
till=2**32
for _ in xrange(input()):
    size=input()
    if size in [99991,99992,99993]:
        one=42952
    elif size in [99994,99995]:
        one=42951
    elif size in [99996,99997,99998]:
        one=42950
    else:
        one=42949
    for i in range(size-1):
        stdout.write('%d '%(one))
    left=till-(one*(size-1))
    two=int(ceil(left/2.0))
    stdout.write('%d\n'%(two))
