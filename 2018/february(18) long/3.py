from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    n=int(stdin.readline())
    tunnel=map(int,stdin.readline().split())
    c,d,s=map(int,stdin.readline().split())
    ans=max(tunnel)*(c-1)
    stdout.write("%d\n"%(ans))
