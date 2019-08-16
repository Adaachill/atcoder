#include <iostream>
#include <string>
using namespace std;

/*
 * input W;
 * output W excluded vowel
 */
int main(){
    string a,b;
    getline(cin,a);
    for(int i = 0;i < a.size();i++){
        if(a[i] == 'a' || a[i] == 'i' || a[i] == 'u' || a[i] == 'e' || a[i] == 'o') ; 
        else b.push_back(a[i]);
    }
    cout << b << endl;
}
