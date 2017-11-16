def between(num,l,r):
    if num>r or num<l:
        return False
    return True
from sys import stdin,stdout
from bisect import insort,bisect,bisect_right
pos=list();neg=list()
n,q,l,r=map(int,stdin.readline().split())
for _ in range(q):
    t,x,y=map(int,stdin.readline().split())
    if t==1:
        pre=x-1
        if pre in pos:
            pos.remove(pre)
        elif pre in neg:
            neg.remove(pre)
        if y>r:
            insort(neg,x-1)
        elif between(y,l,r):
            insort(pos,x-1)
    else:
        ans=0;pre=x-2
        for i in xrange(len(pos)):
            if between(pos[i],x-1,y-1):
                ##find previous
                '''for j in xrange(len(neg)-1,-1,-1):
                    if between(neg[j],pre,pos[i]):
                        pre=neg[j]
                        break'''
                check=bisect_right(neg,pos[i])
                
                if len(neg)!=0 and check!=0 and neg[check-1]>pre:
                    pre=neg[check-1]
                ##find sub array
                end=y
                for j in xrange(len(neg)):
                    if neg[j]>pos[i]:
                        end=min(end,neg[j])
                        break
                ans+=(end-pos[i])
                ##times
                times=max(0,pos[i]-pre-1)
                ans+=(end-pos[i])*times
            pre=max(pos[i],x-2)
        stdout.write("%d\n"%(ans))
