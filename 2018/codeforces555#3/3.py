from sys import stdin,stdout
left,right = dict(),dict()
lpos,rpos = 1,1
for _ in xrange(int(stdin.readline())):
    ty,nu = stdin.readline().split()
    if ty=='L':
        left[nu] = lpos;lpos+=1
    elif ty=='R':
        right[nu] = rpos;rpos+=1
    else:
        if nu in left:
            ans = min(len(left)-left[nu],left[nu]+len(right)-1)
        else:
            ans = min(len(right)-right[nu],right[nu]+len(left)-1)
        stdout.write("%d\n"%ans)