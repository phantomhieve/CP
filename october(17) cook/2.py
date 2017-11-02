from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    num=list(stdin.readline())[:-1]
    two=int(num[-1])%2==0;sum_num=0;check=[0]*len(num);found=False;temp=1
    for i in num:
        sum_num+=int(i)
    ##for last
    if (sum_num-int(num[-1]))%3==0 and int(num[-2])%2==0:
        check[-1]=temp;temp=2;found=True
    if two:
        for i in xrange(len(num)-2,-1,-1):
            if (sum_num-int(num[i]))%3==0 and two:
                check[i]=temp;temp=2;found=True
    if not found:
        stdout.write('-1\n')
    else:
        done=False
        for i in xrange(len(num)-1):
            if done:
                stdout.write(num[i])
            elif check[i]==1:
                done=True
            elif check[i]>1 and num[i]<num[i+1]:
                done=True
            else:
                stdout.write(num[i])
        if done:
            stdout.write(num[-1])
        stdout.write('\n')
