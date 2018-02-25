#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n,m,x,k;
        cin>>n>>m>>x>>k;
        string worker;
        cin>>worker;
        int even=0,odd=0;
        int e_month=m/2,o_month=(m/2)+(m%2);
        //check for even odd
        for(int i=0;i<k;i++){
            if(worker[i]=='E')
                even+=1;
            else
                odd+=1;
        }
        int possible;
        possible=min(even,x*e_month)+min(odd,x*o_month);
        if(possible>=n)
            cout<<"yes\n";
        else
            cout<<"no\n";
    }
}
