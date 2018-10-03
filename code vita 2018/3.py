d = dict()
limit = 1000000
sieve = [True]*limit
for i in xrange(2,limit):
    if sieve[i]:
        for j in xrange(2*i,limit,i):
            sieve[j] = False
prime = list()
for i in xrange(2,limit):
    if sieve[i]:
        prime.append(i)
start = 0
def spiral(X, Y):
    global start
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            if start >= len(prime):
                return 
            d[(x, y)] = prime[start]
            start+=1
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
spiral(260,260)
from sys import stdin,stdout
x = int(stdin.readline())
for _ in xrange(x):
    a,b = map(int,stdin.readline().split(','))
    stdout.write("%d"%(d[(a,b)]))
    if x!=(_+1):
        stdout.write("\n")
