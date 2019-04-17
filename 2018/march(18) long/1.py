from sys import stdin,stdout
for _ in xrange(int(stdin.readline())):
    size = int(stdin.readline())
    hand = map(int,stdin.readline().split())
    glove = map(int,stdin.readline().split())
    front,back=True,True
    for i in xrange(size):
        if hand[i]>glove[i]:
            front = False
        if hand[-1-i]>glove[i]:
            back = False
    if front and back:
        ans = "both\n"
    elif front:
        ans = "front\n"
    elif back:
        ans = "back\n"
    else:
        ans = "none\n"
    stdout.write(ans)
