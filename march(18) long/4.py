from sys import stdin,stdout
from math import ceil,floor
#stdin = open("/Users/atulkhetan/Desktop/input.txt",'r')
#stdout = open("/Users/atulkhetan/Desktop/output1.txt",'w')
def value(mid):
    h=0
    for j in xrange(N):
        h+=int(ceil(float(array[j])/mid))
    return h
for _ in xrange(int(stdin.readline())):
    N,H = map(int,stdin.readline().split())
    array = map(int,stdin.readline().split())
    lower_bound = int(floor(sum(array)/float(H)))
    upper_bound=max(array)
    while lower_bound<upper_bound:
        mid = lower_bound+ (upper_bound-lower_bound)/2
        h=value(mid)
        if H>h:
            upper_bound=mid
        elif h>H:
            lower_bound=mid+1
        else:
            upper_bound=mid
    stdout.write("%d\n"%(lower_bound))
#stdin.close()
#stdout.close()
