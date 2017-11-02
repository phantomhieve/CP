from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    a,b=map(int,stdin.readline().split())
    ans=0;place=0
    while a or b:
        t=(a%10)+(b%10)
        ans+=(t%10)*(10**place)
        a/=10;b/=10;place+=1
    stdout.write("%d\n"%(ans))
    
 
