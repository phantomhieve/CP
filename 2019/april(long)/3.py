from sys import stdin, stdout
from bisect import bisect
cin, cout = stdin.readline, stdout.write
string = cin().strip('\n')
n = len(string)
ans = 0
store = dict()
for i in xrange(n):
    a = ''
    for j in xrange(i,n):
        a+=string[j]
        if a in store:
            temp = store[a]
            ans+= len(store[a]) - bisect(temp, i)
        else:
            store2 = dict()
            for k in xrange(j+1, n):
                b = ''
                for l in xrange(k,n):
                    b+=string[l]
                    if b in store2:
                        if store2[b]==1:
                            store.setdefault(a,[]).append(k)
                    else:
                        new = a+b
                        palin = True
                        for x in xrange(len(new)/2):
                            if new[x]!=new[-1-x]: palin = False
                        if palin:
                            store.setdefault(a,[]).append(k)
                            store2[b] = 1
                            ans+=1
                        else: store2[b] = 0
cout("%d\n"%ans)
