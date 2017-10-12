for _ in range(input()):
    size=input()
    array=list(map(int,raw_input().split()))
    ans=[1]
    check=[ p>0 for p in array]
    for i in range(size-2,-1,-1):
        if check[i] != check[i+1]:
            ans.append(ans[-1]+1)
        else:
            ans.append(1)
    for i in range(size-1,-1,-1):
        print ans[i],
    print ''
    
