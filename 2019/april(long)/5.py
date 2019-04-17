# brute
from sys import stdin, stdout
from collections import deque, defaultdict
cin, cout = stdin.readline, stdout.write
for _ in xrange(int(cin())):
    n, q = map(int, cin().split())
    w = [0] + map(int, cin().split())
    graph = [dict() for i in xrange(n+1)]
    for i in xrange(n-1):
        a, b = map(int, cin().split())
        graph[a][b] = 0
        graph[b][a] = 0
    
    visited =[False for i in xrange(n+1)]
    tree = [list() for i in xrange(n+1)]
    state = deque([1])
    while state:
        p = state.popleft()
        visited[p] = True
        for node in graph[p]:
            if not visited[node]:
                tree[p].append(node)
                state.append(node)
    # take queries
    v, k = 0, 0
    for i in xrange(q):
        a,b = map(int, cin().split())
        v = a^v; k = b^k
    
        a,b = v, k^w[v]
        state = deque([a])
        while state:
            node = state.popleft()
            if w[node]^k > b:
                b = w[node]^k
                a = node
            elif w[node]^k==b:
                a = min(node, a)
            for node_ in tree[node]:
                state.append(node_)
        v, k = a, b
        cout("%d %d\n"%(v, k))