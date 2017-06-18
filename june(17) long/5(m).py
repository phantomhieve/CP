from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    n,k=map(int,stdin.readline().split(' '))
    check=(1<<k)-1
    values=[0]*n
    for i in range(n):
        sets=list(map(int,stdin.readline().split(' ')))
        for elem in sets[1:]:
            values[i]|=(1<<elem)-1
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if(values[i] | values[j]==check):
                ans+=1
    stdout.write(str(ans)+"\n")
            
    
