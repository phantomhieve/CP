for _ in range(input()):
    n,b=map(int,raw_input().split())
    r=n%b;q=n/b
    if((n/b)%2==0):
        ans=(b*(q/2)+r)*(q/2)
    else:
        a=(b*((q/2)+2)+r)*((q/2)-1)
        b=(b*((q/2))+r)*((q/2)+1)
        ans=max(a,b)
    print ans
