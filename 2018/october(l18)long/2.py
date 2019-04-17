from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    N = int(cin()) -1
    times = N/26
    if N%26==0:cout("%d 0 0\n"%pow(2,times))
    elif N%26>=10:cout("0 0 %d\n"%pow(2,times))
    elif N%26>=2:cout("0 %d 0\n"%pow(2,times))
    else: cout("%d 0 0\n"%pow(2,times))
