from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    size = int(cin())
    array = map(int,cin().split())
    arraySorted = sorted(array)
    count,index = 0,size
    for i in xrange(1,size):
        if array[i] < array[i-1]:
            count+=1;index = i-1
    ans = False
    if count<=1:
        ans = True
        array = array[index+1:] + array[:index+1]
        for i in xrange(size):
            if array[i]!=arraySorted[i]:ans = False
    if ans: cout("YES\n")
    else: cout("NO\n")
