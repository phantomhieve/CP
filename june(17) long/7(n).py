for _ in range(input()):
    n,q=map(int,raw_input().split())
    array=map(int,raw_input().split())
    for x in range(q):
        a,b,c,d=map(int,raw_input().split())
        array1=array[a-1:b];array1.sort()
        array2=array[c-1:d];array2.sort()
        ans=0
        for i in range(b-a+1):
            if(array1[i]!=array2[i]):
                ans+=1
        if(ans>1):
            print "NO"
        else:
            print "YES"
