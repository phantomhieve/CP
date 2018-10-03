from math import ceil,log
from sys import stdin,stdout
n,k=map(int,stdin.readline().split())
array=map(int,stdin.readline().split())
table=list()
for i in xrange(n):
    table.append([0]*n)
for i in xrange(n):
    temp=array[i]
    table[i][i]=temp
    for j in xrange(i+1,n):
        temp=min(temp,array[j])
        table[i][j]=temp
xor=[array[0]]
ans_array=[array[0]*array[0]]
for i in xrange(1,n):
    xor.append(array[i]^xor[-1])
    ans_array.append(array[0]*xor[-1])
for i in xrange(1,n):
    for j in xrange(i,n):
        ans=xor[j]^xor[i-1]
        xor.append(ans)
        ans=table[i][j]
        ans_array.append(ans*xor[-1])
ans_array.sort()
stdout.write("%d\n"%(ans_array[k-1]))

    
