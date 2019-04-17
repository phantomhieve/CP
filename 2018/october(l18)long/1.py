from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    a,b,k = map(int,cin().split())
    if ((a+b)/k)%2:cout("COOK\n")
    else:cout("CHEF\n")
