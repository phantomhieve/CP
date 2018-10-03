from sys import stdin,stdout
##stdin=open('/Users/atulkhetan/Desktop/input.txt','r')
##stdout=open('/Users/atulkhetan/Desktop/output.txt','w')
for _ in xrange(int(stdin.readline())):
    x,n=map(int,stdin.readline().split())
    sum_ans=((n*(n+1))/2)-x
    if sum_ans%2==0 and n>3:
        to_find=sum_ans/2
        till = to_find
        for i in xrange(n,0,-1):
            if i==x:
                continue
            to_find-=i
            if i-1>=to_find:
                till=i
                break
        array=[0]*(n+1)
        for i in xrange(till,n+1):
            array[i]=1
        array[to_find]=1
        array[x]=2
        if x==to_find:
            ##for x==1 and x==2
            
            if x==2 :
                array[till]=0
                array[till-1]=1
                array[3]=1
            elif x==1:
                array[till]=0
                array[till-1]=1
                array[2]=1
            else:
                array[1]=1
                array[x-1]=1
        for i in xrange(1,n+1):
            stdout.write("%d"%(array[i]))
        stdout.write("\n")
    else:
        stdout.write("impossible\n")
##stdin.close()
##stdout.close()
    
