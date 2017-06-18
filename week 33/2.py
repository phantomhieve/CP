from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    string=str(stdin.readline())
    one,zero=False,False
    ans=0
    for i in range(len(string)):
        if(string[i]!='1' and string[i]!='0'):
            one=zero=False
        if(string[i]=='1'):
            if(one and zero):
                ans+=1
            one=True;zero=False
        elif(string[i]=='0'):
            zero=True
    stdout.write(str(ans)+'\n')
