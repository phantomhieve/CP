mod=(10**9)+7;
def construct(low,high,pos,array,tree):
    if(low==high):
        tree[pos]=array[low]%mod
        return 
    mid=(low+high)/2
    construct(low,mid,2*pos+1,array,tree)
    construct(mid+1,high,2*pos+2,array,tree)
    tree[pos]=((tree[2*pos+1]%mod)+(tree[2*pos+2])%mod)%mod   
def lazy_p(startrange,endrange,delta,low,high,pos,tree,lazy):
    if(low > high):
        return 
    if(lazy[pos] != 0):
        if(lazy[pos]>0):
            tree[pos]=((tree[pos]%mod)+(lazy[pos]%mod))%mod
            if(low != high):
                lazy[2*pos+1]=((lazy[pos]%mod)+(lazy[2*pos+1]%mod))%mod
                lazy[2*pos+2]=((lazy[pos]%mod)+(lazy[2*pos+2]%mod))%mod
        else:
            tree[pos]=((tree[pos]%mod)-(lazy[pos]%mod)+mod)%mod
            if(low != high):
                lazy[2*pos+1]=(-(lazy[pos]%mod)+(lazy[2*pos+1]%mod)+mod)%mod
                lazy[2*pos+2]=(-(lazy[pos]%mod)+(lazy[2*pos+2]%mod)+mod)%mod
        lazy[pos]=0           
    if(startrange>high or endrange<low):
        return 
    if(startrange<=low and endrange>=high):
        if(delta>0):
            tree[pos]=((delta%mod)+(tree[pos]%mod))%mod
            if(low != high):
                lazy[2*pos+1]=((delta%mod)+(lazy[2*pos+1]%mod))%mod
                lazy[2*pos+2]=((delta%mod)+(lazy[2*pos+2]%mod))%mod
        else:
            tree[pos]=(-(delta%mod)+(tree[pos]%mod)+mod)%mod
            if(low != high):
                lazy[2*pos+1]=(-(delta%mod)+(lazy[2*pos+1]%mod)+mod)%mod
                lazy[2*pos+2]=(-(delta%mod)+(lazy[2*pos+2]%mod)+mod)%mod
        return       
    mid=(high+low)/2
    lazy_p(startrange,endrange,delta,low,mid,2*pos+1,tree,lazy)
    lazy_p(startrange,endrange,delta,mid+1,high,2*pos+2,tree,lazy)
    tree[pos]= ((tree[2*pos+1]%mod)+(tree[2*pos+2]%mod))%mod
def query_p(qlow,qhigh,low,high,pos,tree,lazy):
    if(low>high):
        return 0
    if(lazy[pos] != 0):
        if(lazy[pos]>0):
            tree[pos]=((lazy[pos]%mod)+(tree[pos]%mod))%mod
            if(low != high):
                lazy[2*pos+1]=((lazy[pos]%mod)+(lazy[2*pos+1]%mod))%mod
                lazy[2*pos+2]=((lazy[pos]%mod)+(lazy[2*pos+2]%mod))%mod
        else:
            tree[pos]=(-(lazy[pos]%mod)+(tree[pos]%mod)+mod)%mod
            if(low != high):
                lazy[2*pos+1]=(-(lazy[pos]%mod)+(lazy[2*pos+1]%mod)+mod)%mod
                lazy[2*pos+2]=(-(lazy[pos]%mod)+(lazy[2*pos+2]%mod)+mod)%mod
        
        lazy[pos]=0
    if(qlow>high or qhigh<low):
        return 0
    if(qlow<=low and qhigh>=high):
        return tree[pos]
    mid=(low+high)/2
    return ((query_p(qlow,qhigh,low,mid,2*pos+1,tree,lazy)%mod)+
               (query_p(qlow,qhigh,mid+1,high,2*pos+2,tree,lazy)%mod))%mod
from sys import stdin,stdout
from math import ceil,log
for _ in range(int(stdin.readline())):
    n,m=map(int,stdin.readline().split())
    query,query2=list(),list()
    for i in range(m):
        typ,l,r=map(int,stdin.readline().split())
        query.append([typ,l,r])
        if(typ==2):
            query2.append([l,r,i])
    size=(1<<int(ceil(log(m,2))))*2-1
    tree_m=[0]*size;lazy_m=[0]*size
    construct(0,m-1,0,[1]*m,tree_m)
    for i in range(len(query2)-1,-1,-1):
        temp=query_p(query2[i][2],query2[i][2],0,m-1,0,tree_m,lazy_m)
        lazy_p(query2[i][0]-1,query2[i][1]-1,temp,0,m-1,0,tree_m,lazy_m)
        lazy_p(query2[i][2],query2[i][2],-temp,0,m-1,0,tree_m,lazy_m)
    array=list()
    for i in range(m):
        array.append(query_p(i,i,0,m-1,0,tree_m,lazy_m))
    size=(1<<int(ceil(log(n,2))))*2-1
    tree_m=[0]*size;lazy_m=[0]*size
    for i in range(m):
        if(query[i][0]==1):
            lazy_p(query[i][1]-1,query[i][2]-1,array[i],0,n-1,0,tree_m,lazy_m)
    array=list()
    for i in range(n):
        array.append(query_p(i,i,0,n-1,0,tree_m,lazy_m))
    for i in range(n):
        stdout.write(str(array[i])+" ")
    stdout.write("\n")

        


    
