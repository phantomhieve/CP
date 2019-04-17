from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
MOD = 10**9+7
fact = [1,1]
for i in xrange(2,10000):fact.append((fact[-1]*i)%MOD)
def nCr(a,b):
    first = fact[a]
    second = (fact[b] * fact[a-b])%MOD
    second = pow(second,MOD-2,MOD)
    return (first*second)%MOD
def eff(a,b):
    first = 1
    for i in xrange(a,b,-1):first = (first*i)%MOD
    second = fact[a-b]
    second = pow(second,MOD-2,MOD)
    return (first*second)%MOD
for _ in xrange(int(cin())):
    n,k = map(int,cin().split())
    ans = 0
    for i in xrange(1,k+1):
        first = nCr(k-1,i-1)
        rest = (n-k) - (i-1)
        if rest<0:
            continue
        second = eff(rest+i,rest)
        both = (first*second)%MOD
        ans = (ans +  (pow(2,i,MOD)*both)%MOD)%MOD
    cout("%d\n"%ans)