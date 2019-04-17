from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    n,m = map(int,cin().split())
    A = map(int,cin().split())
    B = map(int,cin().split())
    sumA,sumB = sum(A),sum(B)
    if sumA!=sumB:cout("Alice\n")
    else:
        store = dict()
        for i in xrange(n):
            if A[i]!=0:store[A[i]] = store.setdefault(A[i],0) + 1
        for i in xrange(m):
            if B[i]!=0:store[B[i]] = store.setdefault(B[i],0) - 1
        flag = False
        for i in store:
            if store[i]!=0:flag = True
        #print store
        if flag:cout("Alice\n")
        else:cout("Bob\n")