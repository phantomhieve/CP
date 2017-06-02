string=raw_input()
flip,ans=False,0
for i in xrange(len(string)-1,-1,-1):
    if(string[i]=='0' and flip):
        ans+=1
        flip= not flip
    elif(string[i]=='1' and not flip):
        ans+=1
        flip=not flip
print ans
    
