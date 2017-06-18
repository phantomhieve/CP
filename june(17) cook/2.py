from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    stdout.write(str(n)+'\n')
    for i in range(1,n+1):
        stdout.write(str(n)+'\n')
        for j in range(1,n+1):
            a=(j+i-1)%n
            b=(j+i)%n
            if(a==0):
                a=n
            if(b==0):
                b=n
            p=str(j)+" "+str(a)+" "+str(b)+"\n"
            stdout.write(p)
