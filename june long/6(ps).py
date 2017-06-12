import math,sys
size=int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split(' ')))
store=list()
for i in range(size):
    temp=dict()
    n,exp=array[i],0
    while n%2 == 0:
        exp+=1
        n = n/2
    if(exp):
        temp[2]=exp
    for i in range(3,int(math.sqrt(n))+1,2):
        exp=0
        while n%i == 0:
            exp+=1
            n = n/i
        if(exp):
            temp[i]=exp
    if n > 2:
        temp[n]=1
    store.append(dict(temp))
for _ in range(int(sys.stdin.readline())):
    l,r,x,y=map(int,sys.stdin.readline().split(' '))
    result=0
    for i in range(l-1,r):
        for j in (store[i]):
            if(j>=x and j<=y):
                result+=store[i][j]
    
    sys.stdout.write(str(result)+'\n')
