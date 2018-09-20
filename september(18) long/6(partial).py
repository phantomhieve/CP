from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    m = raw_input()
    n = raw_input()
    temp = list()
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
    array.append(temp)
    n,m = len(n),len(m)
    for i in xrange(1,n):
        for j in xrange(1,m):
            num = int(not(array[i-1][j] | array[i][j-1]))
            array[i].append(num)
    for i in xrange(n):
        for j in xrange(m):
            print array[i][j],
        print 
    stdout.write("\n")
