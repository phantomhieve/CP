from sys import stdin, stdout
cin, cout = stdin.readline, stdout.write
for t in xrange(1, int(cin())+1):
    num = cin().strip('\n')
    size, pos = len(num), -1
    a ,b = ['0']*size,['0']*size
    for i in xrange(size-1, -1, -1):
        if num[i]=='4':
            a[i] = b[i] = '2'
            pos = i
        else: a[i] = num[i]
    a = ''.join(i for i in a)
    if pos == -1: b = '0'    
    else: b = ''.join(b[i] for i in xrange(pos, size))
    cout("Case #%d: %s %s\n"%(t,a,b))