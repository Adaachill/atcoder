#include <iostream>
#include <string>
using namespace std;
/*
 * distinguish 2 string is same with multi letter @
 */
//output word niss
//no type character, but char
int match(char a){
    if(a == '@') return 1;
    else if(a == 'a' || a == 't' || a == 'c' || a == 'o' || a == 'd' || a == 'e' || a == 'r') return 2;
    else return 3;
}

int main(){
    string a,b;
    getline(cin,a);
    getline(cin,b);
    
//    cout << match('@') << match('a') << match('i') << endl;

    int count = 0;//have current state 0 means all same until now
    for(int i = 0;i < a.size();i++){
        if(a[i] == b[i] || (match(a[i])+match(b[i]) == 3)) ;
        else{
            //cout << i << "end" << endl;
            count = 1;
            break;
        }
    }

    //cout << count << endl;

    if(count == 1){
        cout << "You will lose" << endl;
    }else{
        cout << "You can win" << endl;
    }
    return 0;
}
