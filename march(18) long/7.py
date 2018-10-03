from sys import stdin,stdout
from bisect import bisect,bisect_left,insort
from math import ceil,floor,log,sqrt
from os import system
#system('clear')
## building the segment tree
def build(n):
    for i in xrange(n):
        tree[n+i] = [array[i],i]
    for i in xrange(n-1,0,-1):
        tree[i] =  list(tree[i<<1])
        if tree[i<<1][0] < tree[i<<1 | 1][0]:
            tree[i] = list(tree[i<<1 | 1])

## updating the segment tree
def update(index,value):
    tree[index+n] = [value,index]
    i = index + n
    while i > 1 :
        tree[i>>1] = tree[i]
        if tree[i][0]<tree[i^1][0]:
            tree[i>>1] = tree[i^1]
        i >>= 1
## quering in the segment tree
def query(l,r):
    res = [-1,0]
    l,r = l+n,r+n
    while l < r:
        if l&1:
            if res[0]<tree[l][0]:
                res = tree[l]
            l+=1
        if r&1:
            r-=1
            if res[0]<tree[r][0]:
                res = tree[r] 
        l,r = l>>1,r>>1
    return res
## finding the answer
def answer(array_50):
    ans = 0
    for i in xrange(len(array_50)-2):
        if array_50[i][0]<array_50[i+1][0]+array_50[i+2][0]:
            ans = array_50[i][0]+array_50[i+1][0] + array_50[i+2][0]
            break
    return ans
#stdin = open('/Users/atulkhetan/Desktop/code/input.txt','r')
#stdout = open('/Users/atulkhetan/Desktop/code/output.txt','w')
n,q = map(int,stdin.readline().split())
array = map(int,stdin.readline().split())
tree = list()
for i in xrange(4*n):
    tree.append([-1,-1])
build(n)
for _ in xrange(q):
    a,b,c = map(int,stdin.readline().split())
    if a==1:
        update(b-1,c)
    else:
        size = min(45,c-b+1)
        array_50 = list()
        for i in xrange(size):
            array_50.append(query(b-1,c))
            update(array_50[-1][1],-1)
        for i in xrange(size):
            update(array_50[i][1],array_50[i][0])
        ans =answer(array_50)
        stdout.write("%d\n"%(ans))
#stdin.close()
#stdout.close()