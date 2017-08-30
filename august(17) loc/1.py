for _ in range(input()):
    string=raw_input()
    ans=False
    if(len(string)>1):
        for i in range(len(string)-2):
            if(string[i]==string[i+1] or string[i]==string[i+2]):
                ans=True
                break
        if string[-1]==string[-2]:
            ans=True
    if(ans):
        print "YES"
    else:
        print "NO"
