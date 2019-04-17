from sys import stdin,stdout
# seg Tree ------------------------
def combine(node1,node2):
    return max(node1,node2)
def build(size,array,tree):
    for i in xrange(size):
        tree[size+i] = array[i]
    for i in xrange(size-1,0,-1):
        tree[i] = combine(tree[i<<1],tree[i<<1 | 1] )
def query(l,r,size,tree):
    res = - float('inf')
    l,r = l+size,r+size
    while l < r:
        if l&1:
            res = combine(tree[l],res)
            l+=1
        if r&1:
            r-=1
            res = combine(tree[r],res)
        l,r = l>>1,r>>1
    return res
def update(index,size,value,tree):
    i = index + size
    tree[i] = value
    while i > 1 :
        tree[i>>1] = combine(tree[i],tree[i^1])
        i >>= 1
# seg Tree --------------------------
def coinside(a,a_):
    points = list()
    points.extend(a);points.extend(a_)
    points.sort()
    if points[0] in a and points[1] in a_:
        return True
    if points[0] in a_ and points[1] in a:
        return True
    return False
def ksum(k, a):
    n = len(a)
    tree = [0]*(3*n)
    pairs = sorted(zip(a, range(n)))
    i = 0
    minsum = 0
    while i < n:
        equals = []
        equals.append(pairs[i][1])
        j = i + 1
        while j < n and pairs[j][0] == pairs[i][0] and pairs[j][1] - pairs[i][1] <= k:
            equals.append(pairs[j][1])
            i+=1
            j+=1
        m = 0
        for index in equals:
            l = max(0, index-k)
            r = min(n-1, index+k)
            value = query(l,r+1,n,tree)
            if value > m: m = value
        m+=1
        for index in equals:
            update(index,n,m,tree)
            minsum += m
        i+=1
    return minsum
def sum_(array,k,size):
    b = [0]*size
    tree = [0]*(3*size)
    pos = [(array[i],i) for i in xrange(size)] +[(float('inf'),float('inf'))]
    pos.sort(key = lambda item: item[0])
    value_,range_,index_ = pos[0][0],[max(0,pos[0][1]-k),min(size,pos[0][1]+k)],[pos[0][1]]
    for i in xrange(1,size+1):
        range__ = [max(0,pos[i][1]-k),min(size,pos[i][1]+k)]
        if pos[i][0] == value_ and coinside(range_,range__):
            index_.append(pos[i][1])
            range_ = [min(range_[0],range__[0]),max(range_[1],range__[1])]
        else:
            value__ = query(range_[0],range_[1]+1,size,tree) + 1
            for index in index_:
                update(index,size,value__,tree,b)
                b[index] = value__
            value_,range_,index_ = pos[i][0],range__,[pos[i][1]]
    return sum(b)
for _ in xrange(int(stdin.readline())):
    size,s = map(int,stdin.readline().split())
    array = map(int,stdin.readline().split())
    ans = 0
    low, high = 1,size
    while high > low:
        mid = (low+high)//2
        ans = ksum(mid, array)
        if ans > s:
            high = mid-1
        else:
            low = mid+1
    ans = ksum(low, array)
    if size <= s:
        low+=1
    if ans > s:
        low -= 1
    print low


