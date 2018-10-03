def find(pos):
    max_ = [0]*k
    min_ = [float('inf')]*k
    for i in xrange(n):
        for j in xrange(m):
            index = pos[i][j] - 1
            max_[index] = max(max_[index],array[i][j])
            min_[index] = min(min_[index],array[i][j])
    return sum(max_) - sum(min_)
def fillHalf(i,pos,reverse = False,xreverse = False):
    start,end,inc = 0,m,1
    if xreverse: end = n
    if reverse:
        start,end = end-1,start-1
        inc-=2
    put = 0
    for j in xrange(start,end,inc):
        a,b = i,j
        if xreverse:
            a,b = j,i
        if pos[a][b] ==0:
            pos[a][b] = put
        put = pos[a][b]
def fill(pos,pos1,reverse = False):
    end = n
    if reverse: end = m
    for i in xrange(end):
        fillHalf(i,pos,False,reverse)
        fillHalf(i,pos,True,reverse)
        fillHalf(i,pos1,True,reverse)
        fillHalf(i,pos1,False,reverse)
from sys import stdin,stdout
n,m,k = map(int,stdin.readline().split())
pos,pos1,pos2,pos3,array,sort = list(),list(),list(),list(),list(),list()
for i in xrange(n):
    array.append(map(int,stdin.readline().split()))
    pos.append(list([0]*m));pos1.append(list([0]*m));pos2.append(list([0]*m));pos3.append(list([0]*m))
    sort.extend([ [array[-1][j],(i,j)]for j in xrange(m)])
sort.sort(key = lambda item: item[0],reverse = True)
for index in xrange(k):
    i,j = sort[index][1]
    pos[i][j] = index+1; pos1[i][j] = index+1; pos2[i][j] = index+1; pos3[i][j] = index+1
fill(pos,pos1)
fill(pos2,pos3)
fill(pos,pos2,True)
fill(pos1,pos3,True)
pre,ans = find(pos),pos
temp = find(pos1)
if  temp < pre:
    pre = temp
    ans = pos1
temp = find(pos2) 
if  temp < pre:
    pre = temp
    ans = pos2
temp = find(pos3) 
if  temp < pre:
    pre = temp
    ans = pos3
for i in xrange(n):
    for j in xrange(m):
        stdout.write("%d "%(ans[i][j]))
    stdout.write("\n")

