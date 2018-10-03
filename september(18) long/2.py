from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    n,m,x,y = map(int,stdin.readline().split())
    ans = 'Pofik'
    if (n-1)%x==0 and (m-1)%y==0:
        ans = 'Chefirnemo'
    elif (n-2)%x ==0 and (m-2)%y==0 and n-2>=0 and m-2>=0:
        ans = 'Chefirnemo'
    stdout.write("%s\n"%ans)
