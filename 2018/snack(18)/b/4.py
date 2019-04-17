from sys import stdin,stdout
from bisect import bisect
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    n,m,k,l = map(int,cin().split())
    array = sorted(map(int,cin().split())) + [float('inf')]
    totalWait,ans = m*l,float('inf')
    for i in xrange(n+1):
        array[i] = min(array[i],k)
        wait = max(0,totalWait + l - array[i])
        ans = min(ans,wait)
        if totalWait > array[i]+l: totalWait+=l
        else: totalWait = array[i] + l
    cout("%d\n"%ans)