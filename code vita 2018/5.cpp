#include<iostream>
#include<vector>
using namespace std;
#define pb  push_back
#define mp  make_pair
#define int long long
#define itr ::iterator 

typedef pair<int,int>  pii;

const int MAX=1e6;
const int INF=1e12;

int N,res,dp1[MAX],dp2[MAX],arr[MAX];

signed main()
{
	ios_base::sync_with_stdio(false);

	char ch=',';
	cin>>N;
	for(int A=1;A<=N;A++)
	{
		cin>>arr[A];
		if(A!=N)
			cin>>ch;
	}
	dp1[1]=arr[1];
	for(int A=2;A<=N;A++)
		dp1[A]=max(arr[A]+dp1[A-1],2*arr[A]+dp1[A-2]);
	dp2[N+1]=-INF;
	for(int A=N-1;A>=1;A--)
		dp2[A]=max(arr[A+1]+dp2[A+1],2*arr[A+2]+dp2[A+2]);
	res=dp1[N];
	for(int A=0;A+3<=N;A++)
		res=max(res,dp1[A]+3*arr[A+3]+dp2[A+3]);
	cout<<res;
	return 0;
}