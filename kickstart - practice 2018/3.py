from sys import stdin,stdout
stdin = open("/Users/atulkhetan/Desktop/input.txt",'r')
stdout = open("/Users/atulkhetan/Desktop/output.txt",'w')
for _ in xrange(int(stdin.readline())):
    size = int(stdin.readline())
    route,count = dict(),dict()
    for i in xrange(size):
        a = stdin.readline()[:-1]
        b = stdin.readline()[:-1]
        route[a]=b
        if a in count:
            count[a]+=1
        else:
            count[a]=1
        if b in count:
            count[b]+=1
        else:
            count[b]=1
    start = None
    for b in count :
        if count[b]==1 and b in route:
            start = b
    stdout.write("Case #%d:"%(_+1))
    while start in route:
        stdout.write(" %s-%s"%(start,route[start]))
        start = route[start]
    stdout.write("\n")
stdin.close()
stdout.close()
    
