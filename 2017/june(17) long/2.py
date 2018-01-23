for _ in range(input()):
    x,y=map(int,raw_input().split())
    s=((y+x)*(y+x+1))/2
    s+=x
    print s+1
