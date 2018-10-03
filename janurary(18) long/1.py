from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    a,b,c,d=map(int,stdin.readline().split())
    ans='NO'
    if a==b:
        if c==d:
            ans='YES'
    elif a==c:
        if b==d:
            ans='YES'
    elif a==d:
        if b==c:
            ans='YES'
    stdout.write("%s\n"%(ans))
