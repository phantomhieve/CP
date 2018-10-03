from sys import stdin,stdout
from fractions import gcd
def modPower(a,n,mod):
    if n<=0:
        return 1
    if n%2==0:
        x = modPower(a,n/2,mod)
        return (x*x)%mod
    return (a*modPower(a,n-1,mod))%mod
for _ in xrange(int(stdin.readline())):
    a,b,n= map(int,stdin.readline().split())
    second = abs(a-b)
    if second!=0:
        first = (modPower(a,n,second) + modPower(b,n,second))%second
        mod = pow(10,9)+7
        ans = gcd(first,second) % mod
    else:
        mod = pow(10,9)+7
        ans = (modPower(a,n,mod) + modPower(b,n,mod))%mod
    stdout.write("%d\n"%(ans))
