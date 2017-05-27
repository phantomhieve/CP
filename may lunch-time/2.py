parent,cost,d,answer,=dict(),list(),dict(),dict()
def tree(node):
    global parent,cost
    if(node in d):
        return d[node]
    if(node not in parent):
        d[node]=cost[node]
        return cost[node]
    temp=list(parent[node])
    ans=cost[node]
    for i in temp:
        ans=min(ans,tree(i))
    d[node]=ans
    return ans
##--------------------------------------
def traverse(node,par):
    if((node not in parent) and par!=node):
        answer[node]=d[node]+answer[par]
    else:
        temp=list(parent[node])
        for i in temp:
            answer[i]=answer[node]+d[i]
            traverse(i,node)
##----------------------------------------
size=input()
temp=map(int,raw_input().split())
for i in range(size-1):
    if(temp[i]-1 not in parent):
        parent[temp[i]-1]=set()
    parent[temp[i]-1].add(i+1)
cost=list(map(int,raw_input().split()))
for i in range(size):
    temp=tree(i)
answer[0]=cost[0]
traverse(0,0)
