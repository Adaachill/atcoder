#include <iostream>
#include <string>
using namespace std;

int main(){
    string S;
    cin >> S;
    if(S.size() == 2) cout << S;
    else{
        char tmp = S[0];
        S[0] = S[2];
        S[2] = tmp;
        cout << S;
    }
    return 0;
}
