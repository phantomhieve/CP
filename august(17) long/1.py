for _ in range(input()):
    size=input();start=0;check=True
    array=list(map(int,raw_input().split()))
    for i in range(size/2):
        if(array[i]==array[-1-i] and (array[i]==start or array[i]==start+1)):
            check=True
            start=array[i]
        else:
            check=False
            break
    if(check):
        if(array[size/2]==7 and (array[size/2-1]==7 or array[size/2-1]==6)):
            check=True
        else:
            check=False
    if(check):
        print "yes"
    else:
        print "no"
            
        
