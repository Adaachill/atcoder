#include <iostream>
#include <string>
using namespace std;

int main(){
    int A,B,K;
    cin >> A >> B >> K;
    for(int i = 0;i<K/2;i++){
        if(A%2==1){
            A -=1;
        }
        B+=A/2;
        A/=2;

        if(B%2==1){
            B-=1;
        }
        A+=B/2;
        B/=2;
    }
    if(K%2==1){
        if(A%2==1){
              A -=1;
        }
        B+=A/2;
        A/=2;
    }
    cout << A << " " << B << endl;
    return 0;
}
