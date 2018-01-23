from bisect import bisect
t = input()
for _ in xrange(t):
    n, q = map(int, raw_input().split())
    L = map(int, raw_input().split())
    L.sort()
    R = [0]*(n+1)
    for i in xrange(n):
        R[i+1] = R[i] + L[i]
    for i in xrange(q):
        k = int(raw_input())
        idx = bisect(L, k-1)
        ##-----------------------------------
        left = 0; right = idx
        while left+1 < right:
            mid = (left + right) / 2
            su = R[idx] - R[mid]
            need = k * (idx - mid) - su
            print su,need,mid
            if need <= mid:
                right = mid
            else:
                left = mid
        ##------------------------------------
        print n - right
