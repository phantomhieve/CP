## union of two numbers in the data_structure
def union(data1,data2):
    parent1=findset(data1)
    parent2=findset(data2)
    if parent1 == parent2 :
        return
    if store[parent1][1] >= store[parent2][1]:
        store[parent1][1] +=int(store[parent1][1]==store[parent2][1])
        store[parent2][0]=parent1
    else:
        store[parent1][0]=parent2
##return the parent of the node //path compression
def findset(new_node):
    parent=store[new_node][0]
    if new_node==parent :
        return new_node
    store[new_node][0]=findset(store[new_node][0])
    return store[new_node][0]

from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    n,q=map(int,stdin.readline().split())

    ##store is the disjoint set in a list [parent,rank,color]
    store=list();different=[]
    for i in range(n+1):
        store.append([i,0,None])

    ##different stores the index if it is 1
    for i in range(q):
        a,b,c=map(int,stdin.readline().split())
        if c==0:
            union(a,b)
        else:
            different.append([a,b])

    ans=True
    for i in range(len(different)):
        parent1=findset(different[i][0])
        parent2=findset(different[i][1])
        if parent1==parent2:
            ans=0
            break
        ## assigning and checking the colors
        elif store[parent1][2]==store[parent2][2] and store[parent1][2]!=None:
            ans=0
            break
        else:
            if store[parent1][2]==None and store[parent2][2]==None :
                store[parent1][2]=1
                store[parent2][2]=0
            elif store[parent1][2]==None :
                store[parent1][2]=  not store[parent2][2]
            elif store[parent2][2]==None:
                store[parent2][2]= not store[parent1][2]
    if ans:
        stdout.write("yes\n")
    else:
        stdout.write("no\n")
