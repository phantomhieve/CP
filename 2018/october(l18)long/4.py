from timeit import timeit
from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
def brute(a,depth=0):
    global step,ans
    if depth > 20:
        return
    s,s_ = digsum(a),a+m 
    depth+=1
    brute(s,depth)
    brute(s_,depth)
    if s<=ans:
        ans = s;step = min(step,depth) 
    if s_<=ans:
        ans = s_;step = min(step,depth)
def digsum(a):
    a,temp = str(a),0
    for i in a:
        temp+=int(i)
    return temp   
for _ in xrange(int(cin())):
    num,m = map(int,cin().split())
    ans,step = float('inf'),float('inf')
    brute(num)
    if num==ans:
        step = 0
    cout("%d %d\n"%(ans,step))