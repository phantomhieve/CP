from sys import stdin,stdout
n,k = map(int,stdin.readline().split())
k-=1
array = map(int,stdin.readline().split())
countArray = [0]*n
for i in xrange(n):
    if array[i]:
        for j in xrange(max(0,i-k),min(n,i+k+1)):countArray[j] +=1
if all(countArray): 
    for i in xrange(n):
        if array[i]:
            min_ = float('inf')
            for j in xrange(max(0,i-k),min(n,i+k+1)):min_ = min(countArray[j],min_)
            if min_>1:
                array[i] = 0
                for j in xrange(max(0,i-k),min(n,i+k+1)):countArray[j]-=1
    stdout.write("%d\n"%array.count(1))
else:
    stdout.write("-1\n")
