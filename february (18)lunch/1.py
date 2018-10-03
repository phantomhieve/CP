from bisect import bisect
from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    size=int(stdin.readline())
    array=map(int,stdin.readline().split())
    odd,even=0,0
    for i in xrange(size):
        if array[i]%2==0:
            even+=1
        else:
            odd+=1
    if odd%2==0:
        ans=1
    else:
        ans=2
    stdout.write("%d\n"%(ans))
    
