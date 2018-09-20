from sys import stdin,stdout
from math import sqrt,floor
for _ in xrange(int(stdin.readline())):
    size,q= map(int,stdin.readline().split())
    array = map(int,stdin.readline().split())
    for query in xrange(q):
        l,r = map(int,stdin.readline().split())
        count = 0
        for i in xrange(l-1,r):
            start = array[i]
            for j in xrange(i,r):
                start&=array[j]
                if sqrt(start)==floor(sqrt(start)):
                    count +=1
        stdout.write("%d\n"%count)