for _ in range(input()):
    n,k=map(int,raw_input().split())
    array=list()
    check=0
    for i in range(k):
        check+=2**i
    for i in range(n):
        sets=list(map(int,raw_input().split()))
        size=sets[0];sets=list(set(sets[1:]))
        temp=0
        for i in range(len(sets)):
            temp+=(2**(sets[i]-1))
        array.append(temp)
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if(array[i] | array[j]==check):
                ans+=1
    print ans
