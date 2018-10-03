from math import sqrt,ceil
for _ in range(input()):
    n,m=map(int,raw_input().split())
    ans=int(ceil(((sqrt(1+8*m)-1)/2)))
    if(int(ans)>n):
        print -1
    else :
        print ans
