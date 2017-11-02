#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;
int start,stop,bot,top,depth=0;
template <typename T>
void print(T array,int row,int col) {
    for (int i=0; i<col; i++) {
        for (int j=0; j<row; j++) {
            cout<<array[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
}
bool solve(vector<string> &array,int x,int y,string check);
bool canPlace(vector<string> &array,char c,int row,int col);
void changeIt(vector<string> &array,bool (&change)[25][25],int row,int col,char c);
void changeBack(vector<string> &array,bool (&change)[25][25],int row,int col);
int main(){
    //ifstream cin("/Users/atulkhetan/Desktop/input.txt");
    //ofstream cout("/Users/atulkhetan/Desktop/output.txt");
    int t;
    cin>>t;
    for (int test=1; test<t+1; test++){
        vector<string> array;
        int row,col;
        bool ascii[26]={0};
        cin>>col>>row;
        string temp;
        for (int i=0; i<col; i++) {
            cin>>temp;
            for (int j=0; j<row; j++)
                ascii[int(temp[j])-65]=1;
            array.push_back(temp);
        }
        string check="";
        for (int i=0; i<26; i++) {
            if(ascii[i]==1){
                check+=char(65+i);
            }
        }
        bool ans=solve(array,row,col,check);
        if(ans){
            cout<<"Case #"<<test<<":\n";
            for (int i=0; i<col; i++)
                cout<<array[i]<<endl;
        }
        else
            cout<<"i messed up\n";
    }
    //cin.close();
    //cout.close();
    return 0;
}
bool solve(vector<string> &array,int row,int col,string check){
    int x=-1,y=-1;
    bool isThere=false;
    bool change[25][25]={0};
    for (int i=0; i<col; i++) {
        for (int j=0; j<row; j++) {
            if(array[i][j]=='?'){
                x=i;
                y=j;
                isThere=true;
            }
        }
        if(isThere)
            break;
    }
    if(! isThere)
        return true;
    for (int i=0; i<check.length(); i++) {
        start=y;stop=y;bot=x;top=x;
        if(canPlace(array,check[i],row,col)){
            changeIt(array,change,row,col,check[i]);
            if(solve(array,row,col,check))
                return true;
            changeBack(array,change, row, col);
        }
    }
    return false;
}
bool canPlace(vector<string> &array,char c,int row,int col){
    for (int i=0; i<col; i++) {
        for (int j=0; j<row; j++) {
            if(array[i][j]==c){
                start=min(start,j);
                stop=max(stop,j);
                top=min(top,i);
                bot=max(bot,i);
            }
        }
    }
    for (int i=top; i<=bot; i++) {
        for (int j=start; j<=stop; j++) {
            if(array[i][j]!=c && array[i][j]!='?')
                return false;
        }
    }
    return true;
}
void changeIt(vector<string> &array,bool (&change)[25][25],int row,int col,char c){
    for (int i=top; i<=bot; i++) {
        for (int j=start; j<=stop; j++) {
            if(array[i][j]!=c){
                change[i][j]=1;
                array[i][j]=c;
            }
        }
    }
}
void changeBack(vector<string> &array,bool (&change)[25][25],int row,int col){
    for (int i=top; i<=bot; i++) {
        for (int j=start; j<=stop; j++) {
            if(change[i][j]){
                array[i][j]='?';
                change[i][j]=0;
            }
        }
    }
}
