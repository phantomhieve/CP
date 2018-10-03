from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    n,s = map(int,stdin.readline().split())
    array = map(int,stdin.readline().split())
    peak = [1]*n
    x = min(array)
    index = array.index(x)
    # going left
    for i in xrange(index-1,-1,-1):
        if array[i]>array[i+1]:
            peak[i] = peak[i+1]+1
        elif array[i]==array[i+1]:
            peak[i] = peak[i+1]
        else:
            peak[i] = peak[i+1]-1
    # going right
    for i in xrange(index+1,n):
        if array[i] >array[i-1]:
            peak[i] = peak[i-1]+1
        elif array[i]==array[i-1]:
            peak[i]=reak[i-1]
        else:
            peak[i] = peak[i-1]-1
    print peak
