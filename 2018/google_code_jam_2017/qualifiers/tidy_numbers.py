from sys import stdin,stdout
##stdin=open('/Users/atulkhetan/Desktop/B-large-practice.in.txt','r')
##stdout=open('/Users/atulkhetan/Desktop/output.txt','w')
for _ in range(int(stdin.readline())):
    number='0'+str(int(stdin.readline()))
    check=False
    for i in xrange(1,len(number)):
        if not(int(number[i])>=int(number[i-1]) and number[i]!='0'):
            index=i;check=True
            break
    if not check :
        ans=number[1:]
    else:
        ans='9'*(len(number)-index)
        ans_first='';done=False
        for i in range(i-1,0,-1):
            temp=int(number[i])-1
            if (temp<=0 or temp<int(number[i-1])) and i!=1:
                ans_first+='9'
            else:
                if i==1:
                    if temp>0:
                        ans_first+=str(temp);done=True
                else:
                    ans_first+=str(temp)
                    index=i-1
                    break
        ans=ans_first[-1::-1]+ans
        if not done:
            ans=number[1:i]+ans               
    stdout.write('Case #'+str(_+1)+': '+str(ans)+'\n')
##stdin.close()
##stdout.close()
