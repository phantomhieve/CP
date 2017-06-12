from bisect import bisect
mod=(10**9)+7
for _ in range(input()):
    x_i,y_i,z_i=map(int,raw_input().split())
    x=list(map(int,raw_input().split()))
    y=list(map(int,raw_input().split()))
    z=list(map(int,raw_input().split()))
    x.sort()
    z.sort()
    x_sum,z_sum=[x[0]],[z[0]]
    for i in range(1,x_i):
        x_sum.append(x_sum[-1]+x[i])
    for i in range(1,z_i):
        z_sum.append(z_sum[-1]+z[i])
    ans=0
    for i in range(y_i):
        index1=bisect(x,y[i])
        index2=bisect(z,y[i])
        if(index1!=0 and index2!=0):
            x_ans=(((y[i]*index1)%mod) + ((x_sum[index1-1])%mod))
            z_ans=(((y[i]*index2)%mod) + ((z_sum[index2-1])%mod))
            t_ans=(x_ans%mod)*(z_ans%mod)
            ans=((ans%mod)+(t_ans%mod))%mod
    print ans
