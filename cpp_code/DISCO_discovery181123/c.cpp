#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

//まずPとQは全てかけられることになるから、全てのますを入力可能にするためにはP,Q
//の最大値の積がN以下になる必要がある。
//また、P,Qの最大値がa,bと決まった時、PQのありうる組み合わせは
//a^10*b^10となる
//a=1から順番に大きくしていくとN^10-k^10を足し合わせたものが結果となる
int main(){
    int N;
    cin >> N;
    long long  tmp = 0;//最初に１を引く必要はないから
    for(int i=1;i <= N;i++){
        if(i==1) tmp += pow(N,10);
        else{
            tmp+=pow((N-i),10)*pow(i,10)-pow((N-i-1),10)*pow(i,10);
            }
    }
    
    cout << tmp%1000000007 << endl;
    return 0;
}
