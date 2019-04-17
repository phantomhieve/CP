from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    size  = int(stdin.readline())
    array = list()
    for i in xrange(size):
        array.append(list(map(int,stdin.readline().split())))
    ans = 0.0
    for i in xrange(size):
        increase = (array[i][2]/100.0)*array[i][0]
        net = array[i][0]+increase
        decrease = (net/100.0)*array[i][2]
        loss = array[i][0]-(net-decrease)
        ans+=loss*array[i][1]
    stdout.write("%f\n"%(ans))
