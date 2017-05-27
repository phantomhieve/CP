def custom_binary(array,start,end,num):
    if(start<=end):
        mid=start+(end-start)/2
        if(array[mid]>=num):
            if(mid==0):
                return 0
            elif(array[mid-1]>=num):
                return custom_binary(array,start,mid-1,num)
            else:
                return mid
        else:
            return custom_binary(array,mid+1,end,num)
    return end+1
for _ in range(input()):
    n,q=map(int,raw_input().split())
    array=list(map(int,raw_input().split()))
    array.sort()
    size,d=array[-1]+n,dict()
    for z in range(q):
        num=input()
        if(num in d):
            print d[num]
        else:
            if(num>size):
                d[num]=0
                print 0
            else:
                index=custom_binary(array,0,n-1,num)-1
                if(index==-1):
                    print n
                else:
                    ans,start,end=0,0,index
                    while(start<end):
                        if(array[end]+1==num):
                            ans,start,end=ans+1,start+1,end-1
                        elif(num-array[end]<=end-start):
                            ans,start,end=ans+1,start+num-array[end],end-1
                        else:
                            break
                    d[num]=ans+(n-index-1)
                    print ans+(n-index-1)
            
                    
            
        
        
