size,q=map(int,raw_input().split())
array=[0]*size
ans=""
for i in range(q):
    l,r=map(int,raw_input().split())
    for j in range(l-1,r):
        if(array[j]==0):
            array[j]=1
        else:
            array[j]=0
    temp=""
    for j in xrange(size):
        temp+=(str(array[j]))
    ans=max(temp,ans)
print ans
