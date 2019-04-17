from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
from math import ceil,floor
final_ans = 0
def balCount(candies):
    global final_ans
    final_ans = 0
    ans = 0
    for i in xrange(N):
        if A[i]*B[i] > candies:
            ans+= A[i] - long(floor(candies/float(B[i])))
            temp = (long(floor(candies/float(B[i]))))*B[i]
            final_ans = max(final_ans,temp)
        else:
            final_ans = max(final_ans,A[i]*B[i])  
    return ans
N,M = map(int,cin().split())
A = map(int,cin().split())
B = map(int,cin().split())
lo,hi = 0,10**19
while lo < hi:
    mid = (lo+hi)//2
    if balCount(mid) > M: lo = mid+1
    else: hi = mid
balCount(lo)
cout("%d\n"%final_ans)