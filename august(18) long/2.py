from sys import stdin,stdout
end = 35
array = [pow(2,i) for i in xrange(end)]
for _ in xrange(int(stdin.readline())):
    num,ans= int(stdin.readline()),float('inf')
    for i in xrange(end):
        for j in xrange(end):
            if i!=j:
                ans = min(ans,abs(num-(array[i]+array[j])))
    stdout.write("%d\n"%(ans))
