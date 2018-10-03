from sys import stdin,stdout
from math import ceil,log
def add_array(array1,array2):
    temp_array = list([0]*31)
    for i in xrange(31):
        temp_array[i]=array1[i]+array2[i]
    return temp_array
def construct(low,high,pos):
    if(low==high):
        #the base node---------------------------------
        binary = bin(array[low])[2:]
        for j in xrange(len(binary)-1,-1,-1):
            if binary[j]=="1":
                tree[pos][len(binary)-j-1]+=1
        #----------------------------------------------
        return
    mid=(low+high)/2
    construct(low,mid,2*pos+1)
    construct(mid+1,high,2*pos+2)
    #type of query to be performed-----------------
    tree[pos] = add_array(tree[2*pos+1],tree[2*pos+2])
    #----------------------------------------------
def query(qlow,qhigh,low,high,pos):
    if(qlow<=low and qhigh>=high):
        return tree[pos]
    if(qlow>high or qhigh<low):
        ##return something that wont count
        return [0]*31
    mid=(low+high)/2
    ## type of query to be performed
    return add_array(query(qlow,qhigh,low,mid,2*pos+1),
               query(qlow,qhigh,mid+1,high,2*pos+2))
from sys import stdin,stdout
n,q = map(int,stdin.readline().split())
array = map(int,stdin.readline().split())
size=(1<<int(ceil(log(len(array),2))))*2-1
tree =list()
for i in xrange(size):
    tree.append([0]*31)
construct(0,n-1,0)
for _ in xrange(q):
    l,r = map(int,stdin.readline().split())
    value = query(l-1,r-1,0,n-1,0)
    total,ans = r-l+1,0
    for i in xrange(31):
        if not value[i]:
            ans+=1<<i
        elif total-value[i]>total/2:
            ans+=1<<i
    stdout.write("%d\n"%(ans))














