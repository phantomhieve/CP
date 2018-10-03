from bisect import bisect_left as bisect
from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    n= int(stdin.readline())
    array=list()
    ##input
    for i in xrange(n):
        array.append(map(int,stdin.readline().split()))
    ##sorting
    for i in xrange(n):
        array[i].sort()
    ##storing
    ans=list()
    for i in xrange(n):
        ans.append(list(array[i]))
    ##dp
    for i in xrange(1,n):
        for j in xrange(n):
            index=bisect(array[i-1],array[i][j])
            if index == 0:
                ans[i][j]=-1
            else:
                if ans[i-1][index-1]==-1:
                    ans[i][j]=-1
                else:
                    ans[i][j]+=ans[i-1][index-1]
    final_ans=max(ans[-1])
    stdout.write("%d\n"%(final_ans))

                

    
    
