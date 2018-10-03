from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    n,p=map(int,stdin.readline().split())
    if p<3:
        stdout.write("impossible\n")
    else:
        times=n/p
        if p%2==0:
            ans=('a'*((p/2)-1))+'bb'+('a'*((p/2)-1))
        else:
            ans=('a'*(p/2))+('b')+('a'*(p/2))
        ##print ans,times
        ans*=times
        stdout.write("%s\n"%(ans))
