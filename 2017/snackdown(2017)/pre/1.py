for _ in range(input()):
    head,ans=False,True
    size=input()
    array=raw_input()
    for i in range(size):
        if(array[i]=='H'):
            if(head):
                ans=0
                break
            else:
                head=True
        if(array[i]=='T'):
            if(head):
                head=False
            else:
                ans=0
                break
    if(ans and not head):
        print "Valid"
    else:
        print "Invalid"
        
