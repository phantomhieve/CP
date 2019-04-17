from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
mod = 10**9 + 7
def findSum(start):
    return ((2*start + k -1)*k)/2
for _ in xrange(int(cin())):
    n,k = map(int,cin().split())
    start,sum_ = 0,findSum(0)
    while sum_ <= n:
        start+=1
        sum_ = findSum(start)
    start-=1
    if start < 1:cout("-1\n");continue
    left = n - findSum(start)
    array = range(start,start+k)
    for i in xrange(left):array[-i-1]+=1
    ans = 1
    for i in array:
        ans = (ans*((pow(i,2,mod) - (i%mod) + mod)%mod))%mod
    cout("%d\n"%ans)