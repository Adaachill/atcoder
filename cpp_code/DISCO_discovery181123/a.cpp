#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int N;
    cin >> N;
    int tmp = 1;
    for(int i=0;i < N;i++){
        tmp *= 4;
    }
    cout << tmp << endl;
    return 0;
}
