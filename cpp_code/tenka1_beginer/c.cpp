#include <iostream>
#include <string>
using namespace std;
//もらった配列を順位付けして上位のものBと下位のものLに分ける
//BとLで互い違いになるように配置すると最大値をとる
//その時和はsum(B)+sum(L))/2-B(edge)+L(edge)
//よって偶数なら片方の端にはBの最小値を、他方にはLの最大値を配置
//奇数ならLの個数をN/2+1にして端をLの上から２つにすれば良い
int main(){
    int N;
    cin >> N;
    int A[N];

    for(int i=0;i<N;i++){
        int tmp;
        cin >> tmp;
        int k;
        for(int j =i-1;j>=0;j--){
            k=i;//k is swap indicator
            if(A[j]<tmp) k = j;
        }
        A[i] = A[k];
        A[k] = tmp;
    }
    //ordered 
    int sum=0;
    for(int i=0;i<N;i++){
        if(i<N/2) sum+=2*A[i];
        else sum-=2*A[i];
    }
    if(N%2==0){
        sum-=(A[N/2-1]-A[N/2]);
    }else sum+=(A[N/2+1]+A[N/2+2]);
    cout << sum << endl;
    return 0;
}
