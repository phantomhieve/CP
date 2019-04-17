from sys import stdin,stdout
mod = 998244353
n,m = map(int,stdin.readline().split())
a = raw_input()
b = raw_input()
countB,pre,index =[0]*max(n,m),0,0
if n>m: index = n-m
for i in xrange(0,m):
    if b[i]=='1':pre+=1
    countB[i+index]=pre
ans,index = 0,0
if m>n: index = m-n
for i in xrange(n):
    if a[i]=='1':
        ans = (ans + pow(2,n-i-1,mod) * countB[i+index]%mod)%mod
stdout.write("%d\n"%ans)