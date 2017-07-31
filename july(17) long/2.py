for _ in range(input()):
    array=raw_input()
    array+=".";i=0
    ans=0
    while(array[i]=="="and i<len(array)):
        i+=1
    temp=array[i];count=1
    for i in range(i+1,len(array)):
        if(array[i]=="="):
            continue
        if(array[i]==temp):
            count+=1
        else:
            ans=max(ans,count)
            count=1
            temp=array[i]
    print ans+1
        
