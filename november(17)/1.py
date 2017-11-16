from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    string=stdin.readline()
    ans_a,ans_b=0,0
    a,b,temp_a,temp_b=0,0,0,0
    for i in string:
        if i=='.':
            if a:
                temp_a+=1
            if b:
                temp_b+=1
        if i=='A':
            ans_a+=temp_a+1
            temp_a=0;temp_b=0
            a=True;b=False
        if i=='B':
            ans_b+=temp_b+1
            temp_a=0;temp_b=0
            b=True;a=False
    stdout.write("%d %d\n"%(ans_a,ans_b))
    
