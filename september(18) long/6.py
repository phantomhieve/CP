from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    m = stdin.readline()[:-1]
    n = stdin.readline()[:-1]
    array = [[0]]
    array[0][0] = int(n[0]) & int(m[0])
    for i in xrange(1,len(m)):
        ans = int(m[i])
        if array[0][i-1]== 1:
            ans = 0
        array[0].append(ans)
    for i in xrange(1,len(n)):
        ans = int(n[i])
        if array[i-1][0] ==1:
            ans =0
        array.append([ans])
    if len(n)>1 : 
        for i in xrange(1,len(m)):array[1].append(int(not(array[0][i] | array[1][i-1])))
    if len(m)>1 :
        for i in xrange(2,len(n)):array[i].append(int(not(array[i][0] | array[i-1][1])))
    for i in xrange(int(stdin.readline())):
        i,j = map(int,stdin.readline().split())
        i-=1;j-=1
        try:
            ans = array[i][j]
        except:
            try :
                temp = min(i,j)-1
                ans = array[i-temp][j-temp]
            except:
                temp = min(i,j)
                ans = array[i-temp][j-temp]
        stdout.write("%d"%(not ans))
    stdout.write("\n")