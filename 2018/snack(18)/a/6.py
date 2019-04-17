from sys import stdin,stdout
from collections import deque
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    size = int(cin())
    array = map(int,cin().split())
    newArray = list(array)
    k = max(array)
    # if all - 1
    if k==-1:cout('inf\n');continue
    # fixing array right
    check = True
    for i in xrange(1,size):
        if newArray[i-1]!=-1 and newArray[i-1]+1<=k: newArray[i]= newArray[i-1]+1
        if array[i]!=-1 and array[i]!=newArray[i]:check = False
    # fixing array left
    for i in xrange(size-2,-1,-1):
        if newArray[i+1]!=-1 and newArray[i+1]-1>0: newArray[i] = newArray[i+1]-1
        if array[i]!=-1 and array[i]!=newArray[i]:check = False
    # if not possible to fix initially
    if not check: cout('impossible\n');continue
    # finding gaps 
    steps,count = deque(),0
    for i in xrange(size):
        if newArray[i]==-1:count+=1
        elif count!=0: steps.append(count);count=0
    if newArray[0]==-1 :steps.popleft()
    # finding m
    if len(steps)==0: end = 0
    else: end = min(steps)
    M = 0
    for m in xrange(end,-1,-1):
        ans = True
        for i in xrange(len(steps)):
            if (steps[i]-m)%(k+m)!=0:
                ans = False;break
        if ans: M=m;break
    # new k
    k+=M
    # trying to fill the array
    finalArray = list(newArray)
    # fixing array right
    for i in xrange(1,size):
        if finalArray[i-1]!=-1 and finalArray[i-1]+1<=k: finalArray[i]= finalArray[i-1]+1
    # fixing array left
    for i in xrange(size-2,-1,-1):
        if finalArray[i+1]!=-1 and finalArray[i+1]-1>0: finalArray[i] = finalArray[i+1]-1
    # checking the final array with initial array
    check = True
    for i in xrange(size):
        if array[i]!=-1 and array[i]!=finalArray[i]:check = False;break
    if not check:
        # corner case
        corCheck = True
        for i in xrange(size):
            if array[i]!=-1 and array[i]!=1:corCheck = False;break
        #------------
        if corCheck:cout("1\n")
        else:cout('impossible\n')
    else:
        # corner case
        if k==1:
            if finalArray.count(1) >1 : cout("1\n")
            else:cout("inf\n")
        #-----------
        else:
            index = finalArray.index(k)
            count = finalArray.count(k)
            if count > 1 or index!=size-1:cout("%d\n"%k)
            else:cout('inf\n')
    #print array
    #print newArray
    #print finalArray
