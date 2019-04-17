from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    n,k  = map(int,cin().split())
    array = map(int,cin().split())
    left = n-array.count(1)
    if left<=k:cout("YES\n")
    else:cout("NO\n")
