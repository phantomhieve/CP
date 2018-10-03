from sys import stdin,stdout
stdin = open("/Users/atulkhetan/Desktop/input.txt","r")
stdout = open("/Users/atulkhetan/Desktop/output.txt","w")
for _ in xrange(int(stdin.readline())):
    bus = int(stdin.readline())
    route = map(int,stdin.readline().split())
    limit = 6000
    up = [0]*limit
    down = [0]*limit
    for i in xrange(0,len(route),2):
        up[route[i]]+=1
        down[route[i+1]]-=1
    count = 0
    ans =list()
    for i in xrange(limit):
        count+=up[i]
        ans.append(count)
        count+=down[i]
    stdout.write("Case #%d:"%(_+1))
    for i in xrange(int(stdin.readline())):
        stdout.write(" %d"%(ans[int(stdin.readline())]))
    stdin.readline()
    stdout.write("\n")
stdin.close()
stdout.close()
