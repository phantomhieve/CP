def push_heap(A, val):
    A.append(val)
    __siftup(A, len(A) - 1)   
    return
def pop_heap(A):
    n = len(A) - 1
    __swap(A, 0, n)
    max = A.pop(n)
    __siftdown(A, 0)
    return max
def __swap(A, i, j):
    A[i], A[j] = A[j], A[i]
    return  
def __siftdown(A, node):
    child = 2*node + 1

    if child > len(A) - 1:
        return
    if (child + 1 <= len(A) - 1) and (A[child+1] > A[child]):
        child += 1
    if A[node] < A[child]:
        __swap(A, node, child)
        __siftdown(A, child)
    else:
        return   
def __siftup(A, node):
    parent = (node - 1)/2
    if A[parent] < A[node]:
        __swap(A, node, parent)
    if parent <= 0:
        return
    else:
        __siftup(A, parent)
for _ in xrange(input()):
    n,d=map(int,raw_input().split())
    days=list();done=[0]*d;total=0
    for i in xrange(d):
        days.append(list())
    for i in xrange(n):
        d_i,t_i,s_i=map(int,raw_input().split())
        total+=t_i*s_i
        till=min(d,d_i+t_i-1)
        for j in xrange(d_i-1,till):
            push_heap(days[j],s_i)
    for i in xrange(d):
        temp_max=0
        if(len(days[i])>0):
            temp_max=days[i][0]
        temp_loc=i
        for j in xrange(0,i):
            if(len(days[j])>0):
                if(temp_max<days[j][0]):
                    temp_max=days[j][0]
                    temp_loc=j
        done[i]=temp_max
        if(len(days[temp_loc])>0):
            temp=pop_heap(days[temp_loc])
    print total-sum(done)
