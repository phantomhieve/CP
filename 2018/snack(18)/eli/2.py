from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
for _ in xrange(int(cin())):
    n,m,x,y = map(int,cin().split())
    total,ans = n*m,0
    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            if i==x and j==y:continue
            count,inte = 0,False
            count+=m
            if x==i:
                if x>i:count-= (m-x)+1
                else: count-= x
            count+=n-1
            if y==j:
                if y>j: count-= (n-y)+1
                else: count-= y
            #print count,
            #d1
            count+=min(m-j,n-i)
            #print count,
            if x>i and y>j and i-j == x-y:
                count-=min(m-y,n-x) + 1
            #print count,
            count+=min(i-1,j-1)
            if x<i and y<j and i-j ==x-y:
                count-= min(x-1,y-1)+1
            #d2
            count+=min(n-i,j-1)
            if i<x and j>y and i+j == x+y:
                count-=min(n-x,y-1) + 1
            count+=min(i-1,m-j)
            if i>x and j<y and i+j == x+y:
                count-=min(x-1,m-y)+1
            #print count+1
            #print "\n"
            ans += total-(count+1)
    cout("%d\n"%ans)