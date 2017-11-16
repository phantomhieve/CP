from sys import stdin,stdout
store=''
for i in xrange(97,97+26):
    store+=chr(i)
ans_store1='aaaa'
for i in range(33340):
    if i%2==0:
        ans_store1+='ba'
    else:
        ans_store1+='bbaa'
ans_store2={2:['ab',1],3:['aab',2],4:['aabb',2],5:['aaaba',3],6:['aaabab',3],
           7:['aaababb',3],8:['aaababbb',3]}
for i in xrange(int(stdin.readline())):
    size,n=map(int,stdin.readline().split())
    seg=size/n
    extra=size%n
    value=1
    if n!=2 or size==1:
        ans=(store[:n]*seg)+store[:extra]
        if n==1:
            value=size
    else:
        if size in ans_store2:
            value=ans_store2[size][1]
            ans=ans_store2[size][0]
        else:
            ans=ans_store1[:size]
            value=4
    stdout.write("%d %s\n"%(value,ans))
    
