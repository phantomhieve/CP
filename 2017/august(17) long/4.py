for _ in range(input()):
    a=raw_input()
    b=raw_input()
    a_array=[0]*26
    b_array=[0]*26
    for i in range(len(a)):
        a_array[ord(a[i])-97]+=1
        b_array[ord(b[i])-97]+=1
    a_diff,a_max=0,0
    b_diff,b_max=0,0
    same=0
    for i in range(26):
        if(a_array[i]==0 and b_array[i]!=0):
            b_diff+=1
            b_max=max(b_max,b_array[i])
        elif(a_array[i]!=0 and b_array[i]==0):
            a_diff+=1
            a_max=max(a_max,a_array[i])
        elif(a_array[i]!=0 and b_array[i]!=0):
            same+=1
    if(a_diff>0 and a_max>1):
        print "A"
    elif(a_diff>0 and same>0 and b_diff==0):
        print "A"
    else:
        print "B"
