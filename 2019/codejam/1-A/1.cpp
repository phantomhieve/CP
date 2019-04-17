#include<iostream>
using namespace std;
bool possible;
int r,c;
int board[20][20];
void print(){
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            cout<<board[i][j]<< " ";
        }
        cout<<endl;
    }
    cout<<endl<<endl;;
}
bool check(int a, int b, int value){
    for(int i=0; i<r;i++){
        for(int j=0; j<c;j++){
            if(i==a && b==j) continue;
            if(board[i][j]== value) return false;
            if(i==a && board[i][j]==value-1) return false;
            if(j==b && board[i][j]==value-1) return false;
            if(i+j == a+b && board[i][j]==value-1 ) return false;
            if(i-j == a-b && board[i][j]==value-1 ) return false; 
        }
    }
    return true;
}
bool allPossible(int start = 1){
    int solution = true;
    for(int i=0; i< r;i++){
        for(int j=0;j<c;j++){
            if(board[i][j]==-1) solution =false;
            if(board[i][j]==-1 && check(i, j, start)){
                board[i][j] = start;
                if(!allPossible(start+1)){
                    board[i][j] = -1;
                }
                else
                    return true;
            }
        }
    }
    return solution;
}

int main(){
    int t;
    cin>>t;
    for(int tt=1; tt<t+1;tt++){
        cin>>r>>c;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++)
                board[i][j] = -1;
        }
        printf("Case #%d: ",tt);
        if(!allPossible()){
            cout<<"IMPOSSIBLE\n";
        }
        else{
            cout<<"POSSIBLE\n";
            int pos[r*c+1][2];
            int index ;
            for(int i=0;i<r;i++){
                for(int j=0;j<c;j++){
                    index = board[i][j]; 
                    pos[index][0] = i+1;
                    pos[index][1] = j+1;
                }
            }
            //print();
            for(int i=1;i<=r*c;i++)
                printf("%d %d\n",pos[i][0],pos[i][1]);
        }
    }
    return 0;
}