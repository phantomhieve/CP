from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
date = [2010, 2015, 2016, 2017, 2019]
for  _ in xrange(int(cin())):
    num = int(cin())
    if num in date:cout("HOSTED\n")
    else: cout("NOT HOSTED\n")
