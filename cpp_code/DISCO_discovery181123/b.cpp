#include <iostream>
#include <vector>
#include <string>
using namespace std;
//完全に黒なら黒でその個数を数える
//奇数と偶数で場合分け
//中心から数えて１段目から順に個数を数えていく
//偶数なら値はN/2-1、、、、１となるから和は(N/2-1)(N/2)/2で
//奇数なら中心は共有するから（N-2)・４
int main(){
    int N;
    cin >> N;
    int tmp = 0;
    if(N%2==0){
        tmp = N*(N-2)/2;
    }else{
        tmp = (N-3)*(N-3)/2+(N-2);
    }
    cout << tmp << endl;
    return 0;
}
