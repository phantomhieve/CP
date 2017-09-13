mod=(10**9)+7
from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    n,m=map(int,stdin.readline().split())
    query=list()
    for i in range(m):
        temp=map(int,stdin.readline().split())
        if(temp[0]==2):
            temp.append(i)
        query.append(temp)
    a,b,d=list(),list(),list()
    d=[0]*m
    for i in range(m):
        a.append(list())
        b.append(list())
    for i in range(m):
        if(query[i][0]==2):
            a[query[i][2]-1].append(query[i][3])
            b[query[i][1]-1].append(query[i][3])
            d[query[i][3]]=1
    array=[1]*m;factor=0
    for i in range(m-1,-1,-1):
        for j in a[i]:
            factor=(factor+d[j])%mod
        array[i]=(array[i]+factor)%mod
        if(query[i][0]==2):
            d[query[i][3]]=(factor+d[query[i][3]])%mod
        for j in b[i]:
            factor=(factor-d[j]+mod)%mod
    ans=[0]*n
    a,b=list(),list()
    a=[0]*n;b=[0]*n
    for i in range(m):
        if(query[i][0]==1):
            a[query[i][1]-1]=(array[i]+a[query[i][1]-1])%mod
            b[query[i][2]-1]=(array[i]+b[query[i][2]-1])%mod
    factor=0
    for i in range(n):
        factor=(a[i]+factor)%mod
        ans[i]=factor
        factor=(factor-b[i]+mod)%mod
    for i in range(n):
        stdout.write(str(ans[i])+" ")
    stdout.write("\n")
    
            
        

        

    
