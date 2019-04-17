from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
MAX = 25
dp = [list() for i in xrange(MAX)]
for i in xrange(MAX):
    for j in xrange(MAX):
        dp[i].append(list())
def combination(k):
    str_ = ""
    for i in xrange(k+1):
        dp[i][0].append(str_)
        str_+='0'
    for i in xrange(1,k+1):
        for n in xrange(1,i+1):
            for str_ in dp[i-1][n]:
                dp[i][n].append('0'+str_)
            for str_ in dp[i-1][n-1]:
                dp[i][n].append('1'+str_)
combination(17)
for _ in xrange(int(cin())):
    a,b,c = map(int,cin().split())
    if a>b:
        a,b = b,a
    countA = bin(a)[2:].count('1')
    countB = bin(b)[2:].count('1')
    ans = 0
    print bin(c)[2:]
    for i in dp[17][countA]:
        num = int(i,2)
        if num <=c:
            left = c-num
            print num,bin(num)[2:],"   ",left,bin(left)[2:]
            if countB == bin(left)[2:].count('1'):
                #print num,bin(num)[2:],"   ",left,bin(left)[2:]
                ans+=1
    cout("%d\n"%ans)