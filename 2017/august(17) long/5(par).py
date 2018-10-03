n,q=map(int,raw_input().split())
array=list(map(int,raw_input().split()))
for _ in xrange(q):
    t_array=list(map(int,raw_input().split()))
    if(t_array[0]==2):
        for i in xrange(t_array[1]-1,t_array[2]):
            array[i]+=t_array[3]
    else:
        ans=t_array[1]-1
        skip=0
        temp=array[t_array[1]-1]
        for i in range(t_array[1],n):
            if(array[i]>temp and t_array[2]>0 and skip<100):
                t_array[2]-=1
                ans=i
                temp=array[i]
                skip=0
            else:
                skip+=1
        print ans+1
                
