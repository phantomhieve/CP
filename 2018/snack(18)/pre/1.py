from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    n,k = map(int,stdin.readline().split())
    array = map(int,stdin.readline().split())
    array.sort(reverse = True)
    thresh = array[k-1]
    count = 0
    for i in xrange(n):
        if array[i]>=thresh:count+=1
    stdout.write("%d\n"%count)
    