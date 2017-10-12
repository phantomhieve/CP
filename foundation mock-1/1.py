for _ in range(input()):
    n,k=map(int,raw_input().split())
    array=list(map(int,raw_input().split()))
    ans=0
    for i in range(n):
        if (array[i]+k)%7==0:
            ans+=1
    print ans
