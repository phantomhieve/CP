def check(temp_temp,num,size):
    index = size-1
    while num!=0:
        temp = num%10
        temp_temp[index] = temp
        num/=10
        index-=1
    return temp_temp
from sys import stdin,stdout
stdin = open("/Users/atulkhetan/Desktop/input.txt",'r')
stdout = open("/Users/atulkhetan/Desktop/output.txt",'w')
for _ in xrange(int(stdin.readline())):
    num = int(stdin.readline())
    size = len(str(num))
    up,down =0,0
    temp_up,temp_down =[0]*size,[0]*size
    temp_up = check(temp_up,num,size)
    temp_down = check(temp_down,num,size)
    ## just bigger and just lower
    change = False
    for i in xrange(size):
        if temp_up[i]%2!=0 and not change:
            change = True
            ##----------------------------
            temp_up[i]+=1
            index = i
            while index>0 and temp_up[index]==10:
                temp_up[index]=0
                temp_up[index-1]+=2
                index-=1
            ##----------------------------
            temp_down[i]-=1
            index = i
            while index>0 and temp_down[index]<0:
                temp_down[index]=8
                temp_down[index-1]-=2
                index-=1
            ##----------------------------
        elif change:
            temp_up[i]=0
            temp_down[i] = 8
    if temp_up[0]==10:
        temp_up[0]=20
    if temp_down[0] < 0:
        temp_down[0] = 0
    up,down ='',''
    for i in xrange(size):
        up+=str(temp_up[i])
        down+=str(temp_down[i])
    ans = min(abs(int(up)-num),abs(int(down)-num))
    print num,ans
    stdout.write("Case #%d: %d\n"%(_+1,ans))
stdin.close()
stdout.close()


    
            
