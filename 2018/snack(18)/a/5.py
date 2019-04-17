from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    n,m = map(int,cin().split())
    loc = list()
    for i in xrange(n):
        array = cin()
        for j in xrange(m):
            if array[j]=='1':loc.append((i,j))
    ans = [0]*(n+m-1)
    for i in xrange(len(loc)):
        for j in xrange(i+1,len(loc)):
            dist = abs(loc[i][0]-loc[j][0]) + abs(loc[i][1]-loc[j][1])
            if dist<(n+m-1):ans[dist]+=1
    for i in xrange(1,n+m-1):
        cout("%d "%ans[i])
    cout("\n")
