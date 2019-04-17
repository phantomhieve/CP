from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    L,v,l,r = map(int,stdin.readline().split())
    ans = (L/v) - ( (r/v) - ((l-1)/v) )
    stdout.write("%d\n"%ans)