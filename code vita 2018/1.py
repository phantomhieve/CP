from sys import stdin,stdout
def dfs(i_,j_,array):
    for i in xrange(m):
        for j in xrange(n):
            array[i][j] = abs(i-i_)+abs(j-j_)
m,n,k = map(int,stdin.readline().split(','))
array = list()
for i in xrange(k):
    array.append([[0]*n for i in xrange(m)])
for i in xrange(k):
    
    y,x = map(int,stdin.readline().split(','))
    x = abs(x-(m-1))    
    dfs(x,y,array[i])
    '''for x in xrange(m):
        print array[i][x]
    print '\n\n'''
ans = 0
for i in xrange(m):
    for j in xrange(n):
        temp = list()
        for x in xrange(k):
            temp.append(array[x][i][j])
        temp.sort()
        if len(temp)>1 and temp[0]==temp[1]:
            ans+=1
stdout.write("%d"%(ans))            
            

