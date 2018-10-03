##from sys import stdin,stdout
from math import log
stdin=open('/Users/atulkhetan/Desktop/C-small-practice-1.in.txt','r')
stdout=open('/Users/atulkhetan/Desktop/output.txt','w')
def find(num):
    a,b=num/2,num/2
    if num%2==0:
        b-=1
    return a,b
for _ in range(int(stdin.readline())):
    n,k=map(int,stdin.readline().split())
    level=int(log(k+1,2))
    extra=k-((1<<level)-1)
    a,b=find(n)
    array=[[a,b],[1,1]]
    if not extra:
        level-=1
    for i in range(level-1):
        number=list()
        count=list()
        for z in range(len(array[0])):
            a,b=find(array[0][z])
            for k in [a,b]:
                if k in number:
                    count[number.index(k)]+=array[1][z]
                else:
                    number.append(k)
                    count.append(array[1][z])
        array=[number,count]
    if extra==0:
        if k==1:
            value=n
        else:
            value=min(array[0])
    else:
        if array[1][0]>=extra:
            value=array[0][0]
        else:
            value=array[0][1]
    ans1,ans2=find(value)
    ans1=max(0,ans1)
    ans2=max(0,ans2)
    stdout.write('Case #'+str(_+1)+': '+str(ans1)+' '+str(ans2)+'\n')
stdin.close()
stdout.close()
