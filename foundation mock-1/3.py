for _ in range(input()):
    n,k=map(int,raw_input().split())
    array=list(map(int,raw_input().split()))
    array.sort()
    ans=abs(sum(array[:k])-sum(array[k:]))
    print ans
