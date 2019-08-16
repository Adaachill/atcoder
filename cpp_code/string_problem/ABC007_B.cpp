#include <iostream>
#include <string>
using namespace std;

int main(){
    string a;
    getline(cin,a);
    string b;
    b  = 'a';

    if(a == b){
        cout << -1 << endl;
    }else{
        cout << 'a' << endl;
    }
    return 0;
}
