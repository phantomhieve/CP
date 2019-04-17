from sys import stdin,stdout
n,m = map(int,stdin.readline().split())
def subSort(a,b):
    if a[0]>b[0]:
        return 1
    if a[0] < b[0]:
        return -1
    return 0
def problem(a,b):
    if a[0] < b[0]:
        return -1
    if a[0] > b[0]:
        return 1
    if a[1] > b[1]:
        return 1
    if a[1] < b[1]:
        return -1
    return 0
array = list()
for _ in xrange(n):
    temp_a = map(int,stdin.readline().split())
    temp_b = map(int,stdin.readline().split())
    sub = [[temp_a[i],temp_b[i]] for i in xrange(m)]
    sub.sort(subSort)
    ans = 0
    for i in xrange(m-1):
        if sub[i][1] > sub[i+1][1]:
            ans+=1
    array.append([ans,_+1])
array.sort(problem)
for i in xrange(n):
    stdout.write("%d\n"%(array[i][1]))
