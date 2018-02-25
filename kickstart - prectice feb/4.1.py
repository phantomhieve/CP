from math import ceil,log
from sys import stdin,stdout
def construct(low,high,pos):
    if(low==high):
        tree[pos]=new_array[low]
        return
    mid=(low+high)/2
    construct(low,mid,2*pos+1)
    construct(mid+1,high,2*pos+2)
    tree[pos]=tree[2*pos+1]+tree[2*pos+2]

def query(qlow,qhigh,low,high,pos):
    if(qlow<=low and qhigh>=high):
        return tree[pos]
    if(qlow>high or qhigh<low):
        return 0
    mid=(low+high)/2
    return query(qlow,qhigh,low,mid,2*pos+1)+query(qlow,qhigh,mid+1,high,2*pos+2)

stdin = open("/Users/atulkhetan/Desktop/input.txt",'r')
stdout = open("/Users/atulkhetan/Desktop/output.txt",'w')
for _ in xrange(int(stdin.readline())):
    n,q = map(int,stdin.readline().split())
    array = map(int,stdin.readline().split())
    new_array = list()
    for i in xrange(n):
        temp =array[i]
        for j in xrange(i+1,n):
            temp+=array[j]
            new_array.append(temp)
    new_array+=array
    new_array.sort()

    
    size=(1<<int(ceil(log(len(new_array),2))))*2
    tree=[0]*size
    construct(0,len(new_array)-1,0)
    stdout.write("Case #%d:\n"%(_+1))
    for i in xrange(q):
        l,r=map(int,stdin.readline().split())
        stdout.write("%d\n"%(query(l-1,r-1,0,len(new_array)-1,0)))
stdin.close()
stdout.close()
    
