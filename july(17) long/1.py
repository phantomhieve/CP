def convert(string):
    ans=string[0].upper()
    for i in range(1,len(string)):
        ans+=string[i].lower()
    return ans
for _ in range(input()):
    array=raw_input().split()
    ans=""
    if(len(array)>1):
        for i in range(len(array)-1):
            ans+=array[i][0].upper()
            ans+=". "
        ans+=convert(array[-1])
    else:
        ans=convert(array[0])
    print ans
            
            
