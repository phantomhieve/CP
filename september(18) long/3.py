from sys import stdin,stdout
def count_(array,size):
    ans = 0
    for i in xrange(size):
        lo,hi,x=i+1,size,2 
        while lo < hi:
            mid = (lo+hi)//2
            if x < array[mid] ^ array[i]: hi = mid
            else: lo = mid+1
        ans+= size - (lo)
    return ans
for _ in xrange(int(stdin.readline())):
    size = int(stdin.readline())
    array = sorted(map(int,stdin.readline().split()))
    ans = 0
    even,odd = [],[]
    for i in xrange(size):
        if(array[i]%2==0):
            even.append(array[i])
        else:
            odd.append(array[i]) 
    ans = count_(even,len(even)) + count_(odd,len(odd))
    stdout.write("%d\n"%ans)
