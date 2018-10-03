for _ in range(input()):
    size=input()
    array=list(map(int,raw_input().split()))
    if(size%2==1):
        ans=True
        for i in range(size/2):
            if(array[i]!=i+1 or array[i]!=array[-(1+i)]):
                ans=0
                break
        if(ans and array[size/2]==array[size/2+1]+1):
            print "yes"
        else:
            print "no"
    else:
        print "no"
