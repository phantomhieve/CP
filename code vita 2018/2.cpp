#include<iostream>
#include<cmath>
using namespace std;

const int MAX=2e5;

int N,cur,cnt,mark[MAX],prime[MAX];

void sieve()
{
	int ptr=0;
	for(int A=2;A<MAX;A++)
	{
		if(!mark[A])
		{
			prime[ptr++]=A;
			for(int B=A+A;B<MAX;B+=A)
				mark[B]=1;
		}
	}
}

int main()
{
	cin>>N;
	sieve();
	while(prime[cur]*prime[cur]<=N)
	{
		if(!(N%prime[cur]))
		{
			++cnt;
			while(!(N%prime[cur]))
				N/=prime[cur];
		}
		++cur;
	}		
	if(N>1)
		++cnt;
	cout<<pow(2,cnt)-1;
	return 0;
}