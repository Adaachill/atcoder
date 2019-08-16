#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

//Aに最も近い値をN回for loopで回して探す
int main(){
    int N,T,A;
    cin >> N >> T >> A;
    int h[N];
    int tmp;
    int min_dif = 9999;
    for(int i = 0;i < N;i++){
        cin >> h[i];
        if(min_dif > abs(A-T+h[i]*0.006)){
            min_dif = abs(A-T+h[i]*0.006);
            tmp = i;
        }
        
    }
    cout << h[tmp] << endl;
    return 0;
}
