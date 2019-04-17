import math
limit = 100
sieve=[True]*(limit+1);primes = list()
for i in range(2,limit):
    if(sieve[i]==True):
        primes.append(i)
        for j in range(i*2,limit+1,i):
            sieve[j]=False
div = list()
for i in xrange(len(primes)):
    for j in xrange(i+1,len(primes)):
        if primes[i]*primes[j]<=200:
            div.append(primes[i]*primes[j])
ans = dict()
for i in xrange(len(div)):
    for j in xrange(len(div)):
        ans.setdefault(div[i]+div[j],0)
for _ in xrange(input()):
    if input() in ans:print "YES"
    else:print "NO"