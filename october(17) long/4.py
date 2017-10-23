from math import ceil
##stdin=open('/Users/atulkhetan/Desktop/input.txt','r')
##stdout=open('/Users/atulkhetan/Desktop/output.txt','w')
from sys import stdout,stdin
for _ in range(int(stdin.readline())):
    string=stdin.readline()
    a='a'*string.count('a')
    b='b'*string.count('b')
    x,y=map(int,stdin.readline().split())
    seg1=int(ceil(len(a)/float(x)))
    seg2=int(ceil(len(b)/float(y)))
    ##segment one is always greater
    if seg1<seg2:
        a,b=b,a
        seg1,seg2=seg2,seg1
        x,y=y,x
    ans=''
    ##if enough segemts
    if len(b)>= seg1-1:
        array=list()
        size=2*seg1-1
        for i in range(size):
            if i%2==0:
                leng=min(x,len(a))
                array.append(a[0:leng])
                a=a[leng:]
            else:
                array.append(b[0])
                b=b[1:]
        i=1
        if seg1-seg2==0:
            size+=1
            array.append(b[0])
            b=b[1:]
        while b!='':
            leng=min(1,len(b))
            array[i]+=b[:leng]
            b=b[leng:]
            i+=2
            if i>size-1:
                i=1
        for i in range(size):
            ans+=array[i]
                
    ##if not enough segments
    else:
        i=0
        while a!='' or b!='':
            if i%2==0:
                leng=min(x,len(a))
                ans+=(a[0:leng])
                a=a[leng:]
            else:
                leng=min(1,len(b))
                if leng ==0:
                    ans+='*'
                else:
                    ans+=(b[0:leng])
                    b=b[leng:]
            i+=1
            
    stdout.write('%s\n'%(ans))
    
##stdin.close()
##stdout.close()
