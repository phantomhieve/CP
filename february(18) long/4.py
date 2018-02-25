from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    string=stdin.readline()
    size=len(string)-1
    d=[[] for i in xrange(26)]
    for i in xrange(size):
        value=ord(string[i])-97
        d[value].append(i+1)
    odd_count=0
    for i in d:
        if(len(i)%2!=0):
            odd_count+=1
    can_do=False
    if (odd_count==1 and size%2==1) or odd_count==0:
        can_do=True
    if can_do:
        odd=0
        for i in range(26):
            if len(d[i])%2==1:
                odd=d[i].pop()
            for j in xrange(len(d[i])/2):
                stdout.write("%d "%(d[i][j]))
        if odd :
            stdout.write("%d "%(odd))
        for i in range(26-1,-1,-1):
            if len(d[i])%2==1:
                odd=d[i].pop()
            for j in xrange(len(d[i])/2,len(d[i])):
                stdout.write("%d "%(d[i][j]))
        stdout.write("\n")
        
    else:
        stdout.write("-1\n")
