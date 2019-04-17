from sys import stdin,stdout
cin = stdin.readline;cout = stdout.write
MAXN,MOD = 10**6+1 ,10**9+7
fact,pair = [1]*MAXN,[1]*MAXN
for i in xrange(2,MAXN):fact[i] = (fact[i-1]*i)%MOD
for x in xrange(2,MAXN,2): 
    b = (fact[x/2] * pow(2,x/2,MOD))%MOD    
    ans = (fact[x] * pow(b,MOD-2,MOD))%MOD
    pair[x] = ans
for _ in xrange(int(cin())):
    size = int(cin())
    array,counter,uniq= map(int,cin().split()),[0]*MAXN,set()
    array.sort(reverse = True)
    for i in array: counter[i]+=1;uniq.add(i)
    array = sorted(list(uniq),reverse = True)
    ans = 1
    for i in xrange(len(array)):
        count = counter[array[i]]
        if count%2!=0:
            count+=1
            ans = (ans * counter[array[i+1]])%MOD
            counter[array[i+1]]-=1
        ans = (ans * pair[count])%MOD
    cout("%d\n"%ans)