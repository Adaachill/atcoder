#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N,X;
    cin >> N >> X;
    vector<int> a(N);
    vector<int> b(N);
    int max=0;
    int max_it;
    for(int i=0;i < N;i++){
        cin >> a[i] >> b[i];
        if(max < b[i]){
            max_it=i;
            max=b[i];
        }
    }
    a[max_it] +=X;
    //cout << a[max_it] << max << endl;//
    int sum = 0;
    for(int i=0;i<N;i++){
        sum+=a[i]*b[i];
    }
    cout << sum << endl;
    return 0;
}
    
