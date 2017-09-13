from collections import Counter
from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    string = Counter(stdin.readline())
    six,seven,eight=False,False,False
    ans=list()
    if(string["6"]>0):
        six=True
    if(string["7"]>0):
        seven=True
    if(string["8"]>0):
        eight=True
    for i in string:
        if(i !="\n"):
            if(i =="6" or i=="7" or i=="8"):
                if(i=="6" and string["6"]>1):
                    ans.append(chr(66))
                if(i=="7" and string["7"]>1):
                    ans.append(chr(77))
                if(i=="8" and string["8"]>1):
                    ans.append(chr(88))
            if(six==True and int(i)>=5 and i!="6"):
                ans.append(chr(int(str(6)+str(i))))
            if(seven==True and i!="7"):
                ans.append(chr(int(str(7)+str(i))))
            if(eight==True and i!="8"):
                    ans.append(chr(int(str(8)+str(i))))
    if("9" in string and "0" in string):
        ans.append(chr(90))
    ans.sort()
    for i in range(len(ans)):
        stdout.write(ans[i])
    stdout.write("\n")

                
