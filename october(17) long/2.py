from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    n,p=map(int,stdin.readline().split())
    array=list(map(int,stdin.readline().split()))
    cake,hard=0,0
    a=p//2
    b=p//10
    for i in range(n):
        if array[i]>=a:
            cake+=1
        elif array[i]<=b:
            hard+=1
    if cake==1 and hard==2:
        print 'yes'
    else:
        print 'no'
