from sys import stdin, stdout
from collections import deque
cin, cout = stdin.readline, stdout.write
for t in xrange(1, int(cin())+1):
    n = int(cin())
    string = cin().strip('\n')
    size = 2*n-2
    ans = ''
    for ch in string:
        if ch=='S': ans+='E'
        else: ans+='S'
    cout("Case #%d: %s\n"%(t,ans))