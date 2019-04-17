from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    n,x,s = map(int,stdin.readline().split())
    for i in xrange(s):
        a,b = map(int,stdin.readline().split())
        if a == x:
            x = b
        elif b ==x:
            x = a
    stdout.write("%d\n"%x)