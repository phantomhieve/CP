MAX=(10**9)+10
from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    size,find=map(int,stdin.readline().split())
    array=map(int,stdin.readline().split())
    l,r=-1,MAX
    ans=True;
    for i in xrange(size):
        ##first check 2 cases
        ## right wrong
        if array[i]>=r or array[i]<=l:
            ans=False
            break
        ## change
        if array[i]>find:
            r=array[i]
        else:
            l=array[i]
    if ans:
        ans='YES'
    else:
        ans='NO'
    stdout.write("%s\n"%(ans))
