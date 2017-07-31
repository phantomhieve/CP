list_tranie=list();days=dict()
def custom_binary(start,end,num):
    global days
    if(start<=end):
        mid=start+(end-start)/2
        if(days.values()[mid]==num):
            return mid
        elif(days.values()[mid]>num):
            return custom_binary(start,mid-1,num)
        else:
            return custom_binary(mid+1,end,num)
    return end
def custom_merge(start,mid,end):
    global list_tranie
    s1=(mid-start)+1;s2=(end-mid)
    left=list();right=list()
    for i in range(s1):
        left.append(list_tranie[i+start])
    for i in range(s2):
        right.append(list_tranie[i+mid+1])
    left.append([-1]);right.append([-1])
    i=0;j=0
    for k in range(start,end+1):
        if(left[i][0]<right[j][0]):
            list_tranie[k]=right[j]
            j+=1
        else:
            list_tranie[k]=left[i]
            i+=1
def custom_mergesort(start,end):
    global list_tranie
    if(start<end):
        mid=start+(end-start)/2
        custom_mergesort(start,mid)
        custom_mergesort(mid+1,end)
        custom_merge(start,mid,end)
for _ in range(input()):
    n,d=map(int,raw_input().split())
    list_tranie=list();days=dict()
    for i in range(d):
        days[i+1]=i+1
    total=0;done=0;bottom=d
    for i in range(n):
        d_i,t_i,s_i=map(int,raw_input().split())
        list_tranie.append([s_i,d_i,t_i])
        total+=s_i*t_i
    custom_mergesort(0,n-1)
    for i in range(n):
        if(len(days)==0):
            break
        start=custom_binary(0,len(days)-1,list_tranie[i][1])
        if(days.values()[start]!=list_tranie[i][1]):
            start+=1
        while(len(days)>start and list_tranie[i][2]!=0):
            done+=list_tranie[i][0]
            list_tranie[i][2]-=1
            del days[days.values()[start]]
    print total-done
        
