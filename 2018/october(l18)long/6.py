from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
n,m = map(int,cin().split())
MAXN = min(n,m)
MAXANS = 10**6
array = list()
for i in xrange(n): array.append(list(cin())[:-1])
p1,p2,one,two,brute = list(),list(),list(),list(),list()
s1,s2 = '0','1'
for i in xrange(n):
    p1.append('');p2.append('')
    for j in xrange(m):
        if s1=='0': p1[i]+='1';s1 = '1'
        else:p1[i]+='0';s1 = '0'
        if s2=='0': p2[i]+='1';s2 = '1'
        else: p2[i]+='0';s2 = '0'
    s1= p1[i][0];s2 = p2[i][0]
ans = [float('inf')]* (MAXN+1)
check1 = [[0]*(m+1) for i in xrange(n+1)]
check2 = [[0]*(m+1) for i in xrange(n+1)]
for i in xrange(n-1,-1,-1):
    for j in xrange(m-1,-1,-1):
        check1[i][j] = check1[i][j+1] + check1[i+1][j] -check1[i+1][j+1] 
        check2[i][j] = check2[i][j+1] + check2[i+1][j] -check2[i+1][j+1] 
        if p1[i][j] != array[i][j]: check1[i][j]+=1
        if p2[i][j] != array[i][j]: check2[i][j]+=1
for i in xrange(n):
    for j in xrange(m):
        for size in xrange(1,MAXN+1):
            if i + size>n : break
            if j + size>m : break
            count1 = check1[i][j] - check1[i+size][j] - check1[i][j+size] + check1[i + size][j + size]
            count2 = check2[i][j] - check2[i+size][j] - check2[i][j+size] + check2[i + size][j + size]
            ans[size] = min(ans[size],count1,count2)
cin()
query = map(int,cin().split())
for q in query:
    ans_ = 0
    for i in xrange(MAXN+1):
        if ans[i]<=q:
            ans_ = max(ans_,i)
    cout("%d\n"%ans_)