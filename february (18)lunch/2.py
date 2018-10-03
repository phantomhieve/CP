from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    n,m=map(int,stdin.readline().split())
    array=list()
    for i in xrange(n):
        array.append(map(int,stdin.readline().split()))
        for j in xrange(m):
            if array[-1][j]==-1:
                array[-1][j]=-2
            if array[-1][j]==0:
                array[-1][j]=-1
    opt = [[] for _ in xrange(1001)]
    for i in xrange(n):
        for j in xrange(m):
            if array[i][j]>0:
                opt[array[i][j]].append((j,i))
    for i in xrange(1000,0,-1):
        ## x->j y->i
        for x,y in opt[i]:
            if x>0 and array[y][x-1]!=-2 and array[y][x-1]<array[y][x]-1:
                array[y][x-1] = array[y][x]-1
                opt[array[y][x]-1].append((x-1,y))
                
            if y>0 and array[y-1][x]!=-2 and array[y-1][x]<array[y][x]-1:
                array[y-1][x]=array[y][x]-1
                opt[array[y][x]-1].append((x,y-1))
                
            if x<m-1 and array[y][x+1]!=-2 and array[y][x+1]<array[y][x]-1:
                array[y][x+1]=array[y][x]-1
                opt[array[y][x]-1].append((x+1,y))
                
            if y<n-1 and array[y+1][x]!=-2 and array[y+1][x]<array[y][x]-1:
                array[y+1][x]=array[y][x]-1
                opt[array[y][x]-1].append((x,y+1))
        
    for i in xrange(n):
        for j in xrange(m):
            if array[i][j]>=0:
                p='Y'
            elif array[i][j]==-1:
                p='N'
            elif array[i][j]==-2:
                p='B'
            stdout.write(p)
        stdout.write("\n")
