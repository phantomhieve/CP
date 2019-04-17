from sys import stdin,stdout
from math import sqrt,ceil,floor
cin = stdin.readline;cout = stdout.write
def eucDist(x,y,x1,y1):
    return sqrt(pow(x-x1,2)+pow(y-y1,2))
N,Q = map(int,cin().split())
circles = list()
MAXN = 10**6+1
up,down,ans = [0]*MAXN,[0]*MAXN,[0]*MAXN
for _ in xrange(N): circles.append(map(int,cin().split()))
for i in xrange(N):
    for j in xrange(i+1,N):
        dist = eucDist(circles[i][0],circles[i][1],circles[j][0],circles[j][1])
        max_,min_  = max(circles[i][2],circles[j][2]),min(circles[i][2],circles[j][2])
        if  max_ >=  min_ + dist:
            low = max_ - (min_ + dist) 
            high = max_ + dist + min_
        elif dist < circles[i][2] + circles[j][2]:
            low,high = 0,dist +(circles[i][2] + circles[j][2])
        else:
            low,high = dist - (circles[i][2] + circles[j][2]) ,dist +(circles[i][2] + circles[j][2])            
        up[int(ceil(low))]+=1
        down[int(floor(high))]+=1
count = 0
for i in xrange(MAXN):
    count+=up[i];ans[i]+=count;count-=down[i] 
for i in xrange(Q):
    R = int(cin())
    cout("%d\n"%ans[R])