from sys import stdin, stdout
from collections import deque
# assume input array n, m
def possible(k):
    r, c = list(), list()
    index = list()
    for i in xrange(n):
        for j in xrange(m):
            if store[i][j] > k:
                r.append(i)
                c.append(j)
                index.append((i, j))
    if not index: return True
    r_ = max(r) + min(r)
    c_ = max(c) + min(c)
    # enclosing square
    if r_ % 2: cr = [r_//2, r_//2 + 1]
    else :cr = [r_//2]
    if c_ % 2: cc = [c_//2, c_//2 + 1]
    else:cc = [c_//2]
    # try to fix for these pos
    ans = float('inf')
    for x1 in cr :
        for y1 in cc:
            temp  = max( abs(x1-x2) + abs(y1-y2) for x2, y2 in index)
            ans = min(temp, ans)
    return ans <=k

# fill store array, list of '1'
def fill_breadth(Q):
    while Q:
        i,j = Q.popleft()
        # up
        if i-1 >= 0 and store[i-1][j] > store[i][j] + 1:
            store[i-1][j] = store[i][j] + 1
            Q.append((i-1,j))
        # down
        if i+1 < n and store[i+1][j] > store[i][j] + 1:
            store[i+1][j] = store[i][j]+1
            Q.append((i+1,j))
        # left
        if j-1 >= 0 and store[i][j-1] > store[i][j] + 1:
            store[i][j-1] = store[i][j] + 1
            Q.append((i,j-1))
        # right
        if j+1 < m and store[i][j+1] > store[i][j] + 1:
            store[i][j+1] = store[i][j] + 1
            Q.append((i,j+1))
    return 

for t in xrange(int(stdin.readline())):
    n,m = map(int, stdin.readline().split())
    store = [[float('inf')]*m for i in xrange(n)]
    arr, Q = list(), deque()
    for i in xrange(n):
        arr.append(stdin.readline().strip('\n'))
        for j in xrange(m):
            if arr[i][j] == '1': 
                store[i][j] = 0
                Q.append((i,j))
    fill_breadth(Q)
    # do binary search for k
    lo, hi = 0, n+m+1
    while hi > lo:
        mi = (lo + hi)//2
        if possible(mi):hi = mi
        else: lo = mi+1
    stdout.write("Case #%d: %d\n"%(t+1,lo))