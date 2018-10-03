#include<stdio.h>
#include<math.h>
int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n,q;
        scanf("%d%d",&n,&q);
        int mod=1000000007,root=(int)sqrt(n);
        long long int array[n],store[root];
        for(int i=0;i<n;i++){
            scanf("%lld",&array[i]);
            array[i]=(array[i]*array[i])%mod;
        }
        for(int j=0;j<root;j++){
            long long int temp=0;
            for(int i=j;i<n;i+=j+1){
                temp =(temp + array[i])%mod;
            }
            store[j]=temp;
        }
        /*--------------------
        for(int i=0;i<n;i++)
            printf("%lld ",array[i]);
        printf("\n");
        for(int i=0;i<root;i++)
            printf("%lld ",store[i]);
        printf("\n");
        //---------------------*/
        for(int k=0;k<q;k++){
            int type;
            scanf("%d",&type);
            if(type==1){
                int x;
                long long int ans=0;
                scanf("%d",&x);
                if(x<=root)
                    ans=store[x-1];
                else
                    for(int i=x-1;i<n;i+=x)
                        ans=(ans+array[i])%mod;
                printf("%lld\n",ans);
            }
            else{
                int x;
                long long int num;
                scanf("%d%lld",&x,&num);
                long long int update =(num*num)%mod;
                for(int i=0;i<root;i++){
                    if(x%(i+1)==0){
                        store[i]=(store[i]-array[x-1]+mod)%mod;
                        store[i]=(store[i]+update)%mod;
                    }
                }
                array[x-1]=update;
                /*--------------------
                for(int i=0;i<n;i++)
                    printf("%lld ",array[i]);
                printf("\n");
                for(int i=0;i<root;i++)
                    printf("%lld ",store[i]);
                printf("\n");
                //---------------------*/
            }
        }
    }
    return 0;
}