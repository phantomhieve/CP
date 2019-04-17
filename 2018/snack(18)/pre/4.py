from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    size = int(cin())
    a = map(int,cin().split())
    b = map(int,cin().split())
    ans = True
    for i in xrange(size-2):
        if a[i] > b[i]: ans = False;break
        diff = b[i] - a[i]
        a[i] = b[i]
        a[i+1] += 2*diff
        a[i+2] += 3*diff
    if a[-1] != b[-1] or a[-2]!=b[-2]:ans = False
    if ans: cout("TAK\n")
    else: cout("NIE\n")