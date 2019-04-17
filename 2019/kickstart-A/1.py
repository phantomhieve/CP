from sys import stdin, stdout
from array import array
for t in xrange(int(stdin.readline())):
    n, p = map(int, stdin.readline().split())
    arr = array('I',[0]) + array('I' , sorted(map(int, stdin.readline().split())))
    pre = array('L',[0])
    for i in xrange(1, n+1):
        pre.append(pre[i-1]+arr[i])
    ans = float('inf')
    for i in xrange(1, n-p+2):
        total = pre[i+p-1] - pre[i-1]
        total_ = arr[i+p-1]*p
        ans = min(ans, total_ - total)
    stdout.write("Case #%d: %d\n"%(t+1,ans))    