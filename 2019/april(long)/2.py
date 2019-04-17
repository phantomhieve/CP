from sys import stdin, stdout
from fractions import gcd
from collections import deque
from math import floor
cin, cout = stdin.readline, stdout.write
for _ in xrange(int(cin())):
    n = int(cin())
    graph = [dict() for i in xrange(n+1)]
    for i in xrange(n-1):
        a, b = map(int, cin().split())
        graph[a][b] = 0
        graph[b][a] = 0
    v = [0] + map(int, cin().split())
    m = [0] + map(int, cin().split())
    l = [-1 for i in xrange(n+1)]
    visited = [False for i in xrange(n+1)]
    state = deque([[1, v[1]]])
    while state:
        p, value = state.popleft()
        visited[p] = True
        leaf = True
        for node in graph[p]:
            if not visited[node]:
                state.append([node, gcd(value, v[node])])
                leaf = False
        if leaf : 
            l[p] = m[p] - gcd(value, m[p])
    cout(" ".join(str(num) for num in l if num!=-1))
    cout("\n")
