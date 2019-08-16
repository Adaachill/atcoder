#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

//3つの数字のうち１つを２倍した数に書き換えるという操作をK回行う。その時の最大値
//３つの中から最大値を選べそれを2^Kした数と他の数字の和を求める
int main(){
    int a,b,c;
    cin >> a >>  b >> c;
    int k;
    cin >> k;
    int max = a;
    if(b >= a) max = b;
    else if(c >= max) max = c;
    cout << a+b+c+max*pow(2,k)-max << endl;
    return 0;
}

