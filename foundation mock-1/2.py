for _ in range(input()):
    string=raw_input()
    a=dict();b=dict()
    for i in range(len(string)/2):
        if string[i] not in a:
            a[string[i]]=0
        a[string[i]]+=1
    start=len(string)/2
    if not len(string)%2==0 :
        start+=1
    for i in range(start,len(string)):
        if string[i] not in b:
            b[string[i]]=0
        b[string[i]]+=1
    ans=True
    if len(a)==len(b):
        for i in a:
            if (i not in b) or a[i] !=b[i] :
                ans=False
    else:
        ans=False
    if ans:
        print "YES"
    else:
        print "NO"
