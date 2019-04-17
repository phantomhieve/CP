import math
sieve=[True]*(10**5+1)
sieve[0] = sieve[1] = False
def add_prime2(limit):
    for i in range(2,int(math.sqrt(limit))+1):
        if(sieve[i]==True):
            for j in range(i*2,limit+1,i):
                sieve[j]=False
add_prime2(10**5)
print sieve.count(True)