from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    size,k=map(int,stdin.readline().split())
    array=list(map(int,stdin.readline().split()))
    till=max(array)+1
    check_array=[False for i in range(till)]
    for i in array:
        check_array[i]=True
    for i in range(till):
        if k!=0 and not check_array[i]:
            check_array[i]=True
            k-=1
    for i in range(k):
        check_array.append(True)
    missing,ans=False,0
    for i in range(len(check_array)):
        if not check_array[i]:
            missing=True
            ans=i
            break
    if not missing :
        ans=len(check_array)
    stdout.write('%d\n'%(ans))
        
