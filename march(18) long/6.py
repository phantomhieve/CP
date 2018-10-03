from sys import stdin,stdout
from bisect import bisect
for _ in xrange(int(stdin.readline())):
    size = int(stdin.readline())
    array = map(int,stdin.readline().split())
    ans_array,up,down = list([0]*size),list([0]*size),list([0]*size)
    pre_array,suff_array =list([array[0]]),list([array[-1]])
    for i in xrange(1,size):
        pre_array.append(pre_array[-1]+array[i])
        suff_array.append(suff_array[-1]+array[-i-1])
    for i in xrange(size):
        ##for Right
        if i!=size-1:
            index = bisect(pre_array,pre_array[i]+array[i])
            left,right = i+1,min(size-1,index)
            up[left]+=1;down[right]-=1
        ##for Left
        if i!=0:
            index = bisect(suff_array,suff_array[size-1-i]+array[i])
            right,left = i-1,max(0,size-1-index)
            up[left]+=1;down[right]-=1
    count =0
    for i in xrange(size):
        count+=up[i]
        ans_array[i]+=count
        count+=down[i]
        
    for i in xrange(size):
        stdout.write("%d "%(ans_array[i]))
    stdout.write("\n")
            
            
