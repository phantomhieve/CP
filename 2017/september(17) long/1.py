from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    array=list(map(int,stdin.readline().split()))
    s=[array[0]]
    for i in range(1,n):
        s.append(array[i]+s[-1])
    p=[array[-1]]
    for i in range(n-2,-1,-1):
        p.append(array[i]+p[-1])
    ans,temp=0,s[0]+p[-1]
    for i in range(n):
        if(s[i]+p[-1-i]<temp):
            temp=s[i]+p[-1-i]
            ans=i
    stdout.write(str(ans+1)+"\n")
