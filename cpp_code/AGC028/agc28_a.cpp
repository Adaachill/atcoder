#include <iostream>
#include <string>
#include <vector>
using namespace std;

/*
 * length of X, L is M,N baisuu
 * 並び替えが存在しないのでもし、S,Tに割り当てられる部分がなければそこの部分はS,Tの文字を順番に割り当てれば良い
 * また、最短の長さはM,NのLCMである。
 * つまり、割り当てられる墓所が同じ文字列GCD(M,N)の倍数＋１部分に対してS,Tの対応する文字が同じかを先頭から捜査すれば良い。
 */
int func_gcd(int M, int N){
    int less,more;
    if(M>N){
        less = N;
        more = M;
    }else{
        less = M;
        more = N;
    }
    
    int res;//return val
    int temp = less;
    less = more % less;
    if(less > 1){
        more = temp;
        res = func_gcd(more,less);//retrun val must restore or dainyuy
    }else if(less == 1){
        res = 1;
    }else res = temp;//less = 0 divided
    cout << res << endl;
    return res;
}

int main(){
    int N,M;
    string S,T;
    cin >>N >> M;
    cin >> S;
    cin >> T;

    int gcd = func_gcd(M,N);
    
    int bit = 0;
    //割り当てがかぶるのは文字列Sの1＋N/gcd＊K文字目と1＋M/gcd＊k文字目
    for(int i=0;i < gcd;i++){
        if(S[i*N/gcd] != T[i*M/gcd]){
            bit = -1;
            break;
        }
    }
    
    if(bit == 0) cout << N*M/gcd << endl;//==lcm
    else cout << -1 << endl;

    return 0;
}
