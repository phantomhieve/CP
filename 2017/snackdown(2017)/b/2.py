from sys import stdin,stdout
from collections import deque
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    n,m = map(int,cin().split())
    array,MAXN = list(),0
    for i in xrange(n):
        array.append(map(int,cin().split()))
        MAXN = max(MAXN,max(array[i]))
    store = [[float('inf')]*m for i in xrange(n)]
    index = deque()
    for i in xrange(n):
        for j in xrange(m):
            if array[i][j] == MAXN:
                index.append((i,j))
                store[i][j] = 0
    while index:
        i,j = index.popleft()
        ## up
        if i-1 >=0 and store[i-1][j] > store[i][j]+1:
            store[i-1][j] = store[i][j]+1
            index.append((i-1,j))
        ## down
        if i+1  < n and store[i+1][j] > store[i][j]+1:
            store[i+1][j] = store[i][j]+1
            index.append((i+1,j))
        ## left
        if j-1 >=0 and store[i][j-1] > store[i][j]+1:
            store[i][j-1] = store[i][j]+1
            index.append((i,j-1))
        ## right
        if j+1 < m and store[i][j+1] > store[i][j]+1:
            store[i][j+1] = store[i][j]+1
            index.append((i,j+1))
        ## up left and up right
        if i-1 >=0:
            if j-1 >=0 and store[i-1][j-1] > store[i][j]+1:
                store[i-1][j-1] = store[i][j]+1
                index.append((i-1,j-1))
            if j+1 < m and store[i-1][j+1] > store[i][j]+1:
                store[i-1][j+1] = store[i][j]+1
                index.append((i-1,j+1))
        ## down left and down right
        if i+1 < n:
            if j-1 >=0 and store[i+1][j-1] > store[i][j]+1:
                store[i+1][j-1] = store[i][j]+1
                index.append((i+1,j-1))
            if j+1 < m and store[i+1][j+1] > store[i][j]+1:
                store[i+1][j+1] = store[i][j]+1
                index.append((i+1,j+1))
    ans = 0
    for i in store:
        ans = max(ans,max(i))
    cout("%d\n"%ans)