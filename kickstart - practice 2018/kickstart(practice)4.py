'''array = [0,1,2,3,4]
pre = [0,1,3,6,10]
pre_ = [0,1,4,10,20]
size = 5'''
'''
1 3 6 10
2 5 9
3 7
4
'''
'''
1 2 3 3 4 5 6 7 9 10 
'''
sum_= 0
def findSum(index):
    global sum_,count_
    value,sum_ = findBefore(index),0
    count = findCount(value)
    sum_ -=  (count-index-1)*value
    return sum_
def findBefore(index):
    value = 100*size
    lo,hi = 0,value
    while lo < hi:
        mid = (lo+hi)//2
        if index < findCount(mid): hi = mid
        else: lo = mid+1
    return lo
def findCount(num):
    global sum_
    ans= 0
    for i in xrange(1,size):
        lo,hi = i,size
        while lo < hi:
            mid = (lo+hi)//2
            if num < pre[mid] - pre[i-1]: hi = mid
            else: lo = mid+1
        sum_ += max(0,pre_[lo-1] - pre_[i-1] - (pre[i-1]*(lo -i)))
        ans += (lo - i)
    return ans
from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    size,q = map(int,stdin.readline().split())
    array = [0] + list(map(int,stdin.readline().split()))
    pre,pre_ = [0],[0]
    size+=1
    for i in xrange(1,size):
        pre.append(array[i]+pre[-1])
        pre_.append(pre_[-1]+pre[i])
    stdout.write("Case #%d:\n"%(_+1))
    for j in xrange(q):
        l,r = map(int,stdin.readline().split())
        first = l-2
        if(first>=0):
            first = findSum(first)
        else:
            first = 0
        last = findSum(r-1)
        stdout.write("%d\n"%(last-first))



