from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    size = int(stdin.readline())
    array = map(int,stdin.readline().split())
    array.sort()
    ans =0
    for i in xrange(1,size):
        if array[i]==array[i-1]:
            ans+=1
    stdout.write("%d\n"%(ans))
