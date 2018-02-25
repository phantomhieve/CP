#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        string array[24]={"hcfe", "echf", "chef", "fech", "fehc", "cehf", "cefh", "cfhe", "fche", "hefc", "ehfc", "ehcf", "efch", "hfce", "chfe", "hfec", "fhce", "fhec",
         "fceh", "cfeh", "efhc", "hcef", "ecfh", "hecf"};
        string var,temp="1234";
        cin>>var;
        int ans=0;
        if(var.length()>=4){
            temp[1]=var[0];
            temp[2]=var[1];
            temp[3]=var[2];
        }
        for(int i=3;i<var.length();i++){
            int value = (int)tolower(var[i]);
            if(value>=97 && value<=122){
                temp=temp.substr(1,3)+var[i];
                for(int j=0;j<24;j++){
                    if(temp==array[j])
                        ans+=1;
                }
            }
        }
        if(ans!=0)
            cout<<"lovely "<<ans<<endl;
        else
            cout<<"normal"<<endl;
    }
    return 0;
}
