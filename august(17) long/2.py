from math import ceil
for _ in range(input()):
    n,d=map(int,raw_input().split())
    array=list(map(int,raw_input().split()))
    average=sum(array)/float(n);steps=0
    if(ceil(average)!=average):
        print -1
        continue
    average=int(average)
    for i in range(n):
        if(array[i]!=average):
            if(i+d<n):
                temp=array[i]-average
                array[i]=average
                array[i+d]+=temp
                steps+=abs(temp)
    check=True
    for i in range(n):
        if(array[i]!=average):
            print -1
            check=False
            break
    if(check):
        print steps
            
