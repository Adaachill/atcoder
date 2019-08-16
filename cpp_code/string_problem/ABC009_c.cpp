#include <iostream>
#include <string>
#include <vector>
using namespace std;
//sort input string N and put rank in dictionary order
void sort(string s,vector<int>& rank){
    //vector<int> rank(s.size();
    for(int i = 0;i < s.size();i++){
        rank[i] = i;
        for(int j = 0;j < i;j++){
            if(s[j] > s[i]){
                rank[j] += 1;
            }
            if(s[j] <= s[i]){
                rank[i] += 1;
            }
        }
    }
}

int main(){
    string N;
    int K;
    string S;
    
    cin >> N;
    cin >> K;

    vector<int> rank(N.size());
    sort(N,rank);

    for(int i = 0;i < rank.size();i++){
        cout << rank[i];
    }

    return 0;
}
