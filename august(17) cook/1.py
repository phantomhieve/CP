from math import sqrt
for _ in range(input()):
    a,b,c=map(int,raw_input().split());
    if((a*sqrt(2))/b>float(a)*2/c):
        print "Elevator"
    else:
        print "Stairs"
