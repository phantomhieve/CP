for _ in range(input()):
    string=raw_input()
    array=[0]*len(string)
    d={string[-1]:0}
    for i in range(len(string)-1,0,-1):
        cost=abs(ord(string[i])-ord(string[i-1]))
        if(string[i-1] in d):
            array[i-1]=min(d[string[i-1]],array[i]+cost)
            d[string[i-1]]=array[i-1]
        else:
            d[string[i-1]]=cost+array[i]
            array[i-1]=cost+array[i]
    print array[0]
   
    
