from sys import stdin,stdout
##stdin=open('/Users/atulkhetan/Desktop/A-large-practice.in.txt','r')
##stdout=open('/Users/atulkhetan/Desktop/output.txt','w')
for _ in range(int(stdin.readline())):
    line=stdin.readline().split()
    string=[p=='+' for p in line[0]]
    flip=int(line[1])
    ans=0;i=0
    while(i<len(string)-flip+1):
        if not string[i]:
            string[i:i+flip]=[not p for p in string[i:i+flip]]
            ans+=1
        i+=1
    if(all(string)):
        stdout.write('Case #'+str(_+1)+': '+str(ans)+'\n')
    else:
        stdout.write('Case #'+str(_+1)+': IMPOSSIBLE\n')
##stdin.close()
##stdout.close()
