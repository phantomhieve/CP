d = dict()
from sys import stdin,stdout
from collections import deque
from fractions import gcd
def find(str1,str2,fact1,fact2):
    if fact1 > fact2:
        str1,str2 = str2,str1
        fact1,fact2 = fact2,fact1
    left , curr_index = fact2,0
    count = 0
    if str1+str2 in d:
        return d[str1+str2]
    for i in xrange(len(str1)):
        if left >= fact1:
            left-=fact1
            if str1[i]==str2[curr_index]:
                count +=fact1
        elif left < fact1:
            if left!=0:
                if str1[i]==str2[curr_index]:
                    count += left
            curr_index+=1
            if str1[i]==str2[curr_index]:
                    count += fact1-left
            left = fact2 - (fact1-left)
    d[str1+str2] = count
    return count
for _ in xrange(int(stdin.readline())):
    d.clear()
    array,array1  = list(),list()
    n,m = map(int,stdin.readline().split())
    array = raw_input()
    n1,m1 = map(int,stdin.readline().split())
    array1 = raw_input()
    N = (n*n1)//gcd(n,n1)
    M = (m*m1)//gcd(m,m1)
    # assuming n is bigger
    if n1>n:
        n,n1 = n1,n
        m,m1 = m1,m
        array,array1 = array1,array
    index = list()
    fact1,fact2 = N//n,N//n1
    left , curr_index = fact2,0
    for i in xrange(n):
        indexes = list()
        if left >= fact1:
            left-=fact1
            indexes.append(tuple([curr_index,fact1]))
        elif left < fact1:
            if left!=0:
                indexes.append(tuple([curr_index,left]))
            curr_index+=1
            indexes.append(tuple([curr_index,fact1-left]))
            left = fact2 - (fact1-left)
        index.append(list(indexes))
    fact1,fact2 = M//m,M//m1
    ans = 0
    for i in xrange(n):
        start = i * m
        str1 = array[start:start+m]
        for idx,val in index[i]:
            start = idx*m1
            str2 = array1[start:start+m1]
            ans+=(find(str1,str2,fact1,fact2))*val
    stdout.write("%d\n"%(ans))


