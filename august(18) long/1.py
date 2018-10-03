from sys import stdin,stdout
for i in xrange(int(stdin.readline())):
    top = stdin.readline()
    bot = stdin.readline()
    b,o,mix=0,0,0 
    for i in xrange(3):
        if top[i]=='b' and bot[i]=='o':
            mix+=1
        elif top[i]=='o' and bot[i]=='b':
            mix+=1
        elif top[i]=='b' or bot[i]=='b':
            b+=1
        elif top[i]=='o' or bot[i]=='o':
            o+=1
    if o<1 and mix:
        o+=1
        b+=mix-1
    else:
        b+=mix
    if b>=2 and o>=1:
        stdout.write("yes\n")
    else:
        stdout.write("no\n")


