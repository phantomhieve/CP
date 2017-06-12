from sys import stdin,stdout
size=input()
a=list(map(int,stdin.readline().split(' ')))
b=list(map(int,stdin.readline().split(' ')))
a_min1=min(a);a_pos=a.index(a_min1)
del a[a_pos];a_min2=min(a)
b_min1=min(b);b_pos=b.index(b_min1)
del b[b_pos];b_min2=min(b)
if(a_pos==b_pos):
    if(a_min1==b_min1):
        ans=a_min1+min(a_min2,b_min2)
    else:
        ans=min(a_min1+b_min2,b_min1+a_min2)
else:
    ans=a_min1+b_min1
stdout.write(str(ans)+"\n")
