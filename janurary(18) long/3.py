from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    n,k=map(int,stdin.readline().split())
    array=map(int ,stdin.readline().split())
    times=3
    if k<=3:
        times=k
    temp=array*times
    ##ans1
    a,ans1=array[0],array[0]
    for i in xrange(1,len(temp)):
        a=max(temp[i],temp[i]+a)
        ans1=max(a,ans1)
    ##ans2
    if k>3:
        left=list(array)
        right=list(array)
        for i in xrange(n-2,-1,-1):
            left[i]+=left[i+1]
        for i in xrange(1,n):
            right[i]+=right[i-1]
        ans2=(sum(array)*(k-2))+(max(left)+max(right))
        ans1=max(ans1,ans2)
    stdout.write("%d\n"%(ans1))
        
