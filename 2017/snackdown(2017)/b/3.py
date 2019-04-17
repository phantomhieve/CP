from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    size = int(cin())
    array = list()
    count = list()
    for i in xrange(2):
        array.append(cin())
        count.append(array[i].count("*"))
    ans = 0
    if count[0] > 0 and count[1] > 0:
        ans = 1
        a = b = 0
        for i in xrange(size):
            if array[0][i] == "*":a+=1
            if array[1][i] == "*":b+=1    
            if a>1 or b>1:
                a = b= 0
                ans+=1
                if array[0][i] == "*":a+=1
                if array[1][i] == "*":b+=1 
    else:
        ans = max(count[0],count[1])-1
    cout("%d\n"%max(0,ans))