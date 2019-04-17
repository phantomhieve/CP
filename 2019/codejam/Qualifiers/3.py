from sys import stdin, stdout
from fractions import Fraction
cin, cout = stdin.readline, stdout.write
for t in xrange(1, int(cin())+1):
    n, l = map(long, cin().split())
    arr = map(long, cin().split())
    primes = dict()
    for i in xrange(l):
        for j in xrange(i,l):
            v = str(Fraction(arr[i],arr[j]))
            v_ = str(arr[i]) + '/' + str(arr[j])
            if v!='1' and v!=v_:
                values = v.split('/')
                primes[values[0]] = 0
                primes[values[1]] = 0
                e = arr[i]/long(values[0])
                primes[str(e)] = 0
    found = 0
    primes = sorted([long(prime) for prime in primes]) 
    index = [0 for i in xrange(l+1)]
    for i in xrange(1,l):
        v = str(Fraction(arr[i-1],arr[i]))
        v_ = str(arr[i-1]) + '/' + str(arr[i])
        if v!='1' and v!=v_:
            values = v.split('/')
            index[i-1] = long(values[0])
            index[i+1] = long(values[1])
            index[i] =  arr[i]/long(values[1])
            found = i
    for i in xrange(found, l):
        if index[i+1]==0:
            index[i+1] = arr[i]/index[i]
    for i in xrange(found, 0, -1):
        if index[i-1] == 0:
            index[i-1] = arr[i-1]/index[i]
    ans = "".join( chr(ord('A') + primes.index(num)) for num in index)
    cout("Case #%d: %s\n"%(t, ans)) 