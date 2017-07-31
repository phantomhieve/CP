array=[2,7]
for i in xrange(2,30):
    if(i%2==1):
        ans=array[i-1]+7
        array.append(ans)
    if(i%2==0):
        ans=array[i-1]+3*array[i-2]
        array.append(ans)
d={}
def subset(array,l,r,ans):
    if (l > r):
        d[ans]=0
        return
    subset(array, l+1, r, ans+array[l]);
    subset(array, l+1, r, ans);
subset(array,0,4,0)
for _ in range(input()):
    num=input()
    if num in d:
        print "YES"
    else:
        print "NO"

