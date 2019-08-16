#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

//a bまでにx x となる日が何日あるか？
//まずa b を比べて、a <= b cout << a, else  cout a-1
int main(){
    int a,b;
    cin >> a >>  b;
    if(b >= a) cout << a << endl;
    else cout << a-1 << endl;
    return 0;
}

