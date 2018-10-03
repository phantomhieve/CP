def lcs(X , Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for i in xrange(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
    return L[m][n]
from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    size1,size2=map(int,stdin.readline().split())
    string1=map(str,stdin.readline())
    string2=map(str,stdin.readline())
    a,b='_','_'
    s1,s2=0,0
    for i in xrange(size1):
        if string1[i]!=a[s1]:
            s1+=1
            a+=string1[i]
    for i in xrange(size2):
        if string2[i]!=b[s2]:
            s2+=1
            b+=string2[i]
    a=a[1:];b=b[1:]
    ans = lcs(a,b)
    final_ans=s1+s2-ans
    stdout.write("%d\n"%(final_ans))
    
        
