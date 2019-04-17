from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    size = int(cin())
    array = map(int,cin().split())
    pre = [array[0]]
    for i in xrange(1,size):pre.append(pre[-1]+array[i])
    day,people = 1,array[0]
    while people +1  < size:
        people+=pre[people]
        day+=1
    cout("%d\n"%day)