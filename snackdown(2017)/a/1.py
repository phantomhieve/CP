for _ in xrange(input()):
    n,m=map(int,raw_input().split())
    for i in range(m):
        a,b=map(int,raw_input().split())
        if(a==b):
            n-=1
        else:
            n-=2
    if(n%2==0):
        print "yes"
    else:
        print "no"
    
