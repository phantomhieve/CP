#include<iostream>
#include<vector>
#include<cstring>
using namespace std;
#define int long long
#define limit 100002
int profit(vector<int> tree[], int root, int x);
int arr[limit];
bool visited[limit];
signed main(){
    int t;
    cin>>t;
    while(t--){
        memset(visited, false, limit);
        int n, x;
        cin>>n>>x;
        for(int i=1; i<=n; i++){
            cin>>arr[i];
        }
        vector<int> tree[limit];
        for(int i=0;i<n-1;i++){
            int a,b ;
            cin>>a>>b;
            tree[a].push_back(b);
            tree[b].push_back(a);
        }
        cout<<profit(tree, 1, x)<<endl;
    }
}
int profit(vector<int> tree[], int root, int x){
    visited[root] = true;
    int sum = arr[root];
    vector<int>::iterator ptr;
    for (ptr = tree[root].begin(); ptr < tree[root].end(); ptr++){
        if(! visited[*ptr])
            sum+=profit(tree, *ptr, x);
    }
    return max(sum, -x);
}