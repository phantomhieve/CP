from math import sqrt
from fractions import gcd
from sys import stdin,stdout
from collections import deque
cin = stdin.readline;cout = stdout.write
sieve,prime=range(51),set()
for i in range(2,51):
    if(sieve[i]==i):
        prime.add(i)
        for j in range(i*2,50+1,i):
            if sieve[j]==j: sieve[j] = i
def getFactorization(x):
    ans=list()
    while x!=1:
        ans.append(sieve[x])
        x=x/sieve[x]
    return ans
def connect():
    conn =0
    for start in xrange(size):
        if not visited[start]:
            conn+=1
            dfs(start)
    return conn
def dfs(start):
    check = deque([start])
    while check:
        node = check.popleft()
        visited[node] = True
        for conn in graph[node]:
            if not visited[conn]:check.append(conn)
for _ in xrange(int(cin())):
    size = int(cin())
    array = map(int,cin().split())
    graph = [dict() for i in xrange(size)]
    primeGot = []
    for i in xrange(size):
        primeGot.extend(getFactorization(array[i]))
        for j in xrange(i+1,size):
            if gcd(array[i],array[j]) == 1: graph[i][j] =0;graph[j][i] = 0
    visited = [False]* size
    conn = connect()
    primeGot = set(primeGot)
    if conn>1:
        left = list(prime - primeGot)
        array[0] = left[0]
    if conn>1: cout("1\n")
    else:cout("0\n")
    for i in xrange(size):
        cout("%d "%array[i])
    cout("\n")