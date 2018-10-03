#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
#define FOR(i,end) for(i=0;i<end;i++)
int  __gcd(int a,int b){return b == 0 ? a :__gcd(b, a % b);}
int find(string,string,int,int);
signed main(){
    int t;
    cin>>t;
    while(t--){
        int n,m,n1,m1,N,M,temp,fact1,fact2,left,curr_index,i,j,f1,f2;
        string arr,arr1,tem;
        cin>>n>>m;
        cin>>arr;
        cin>>n1>>m1;
        cin>>arr1;
        N = (n*n1)/__gcd(n,n1);
        M = (m*m1)/__gcd(m,m1);
        if(n1>n){
            swap(n,n1);
            swap(m,m1);
            swap(arr,arr1);
        }
        fact1 = N/n;fact2 = N/n1;
        f1 = M/m;f2 = M/m1;
        left = fact2; curr_index = 0;
        long ans = 0;
        FOR(i,n){
            string a = arr.substr(i*m,m);
            string b = arr1.substr(curr_index*m1,m1);
            if(left>=fact1){
                left-=fact1;
                ans+= find(a,b,f1,f2)*fact1;
            }
            else{
                if(left!=0){
                    ans+= find(a,b,f1,f2)*left;
                }
                curr_index+=1;
                b = arr1.substr(curr_index*m1,m1);
                ans+= find(a,b,f1,f2)*(fact1-left);
                left = fact2 - (fact1-left);
            }
        }
        cout<<ans<<endl;
    }
}
int find(string str1,string str2,int fact1,int fact2){
    if(fact1>fact2){
        swap(str1,str2);
        swap(fact1,fact2);
    }
    int left =fact2,curr_index = 0,count = 0,i;
    FOR(i,str1.length()){
        if(left >= fact1){
            left-=fact1;
            if(str1[i]==str2[curr_index])
                count +=fact1;  
        }
        else{
            if(left!=0){
                if(str1[i]==str2[curr_index])
                    count += left;
            }
            curr_index+=1;
            if(str1[i]==str2[curr_index])
                count += fact1-left; 
            left = fact2 - (fact1-left);
        }
    }
    return count;
}