from sys import stdin,stdout
size = int(stdin.readline())
if size!=1:
    a,b = size/2 + size%2,size/2
    start = 2
    for i in xrange(a-1):
        stdout.write("%d "%start)
        start+=1
    stdout.write("1 ")
    start+=1
    for i in xrange(b-1):
        stdout.write("%d "%start)
        start+=1
    stdout.write("%d\n"%(a+1))
    stdout.write("%d "%size)
    for i in xrange(1,size):
        stdout.write("%d "%i)
    stdout.write("\n")
else:
    stdout.write("1\n1\n")