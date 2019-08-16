#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

//隣接する２つのますを塗ることを繰り返して入力で与えられる点描を書くことが着るか判定する
//上下左右に隣接しているますをひとまとめにした時にその全てのブロックにおいてますが２つ以上で成り立っていれば良い。
//計算量を考えるならユニオンファインド？(今回はクラスタリングする必要はないので必要ないけど。クラスターに属する数の最大値とかなら使うかも）
//ナイーブに行くならh,wでループを回して隣接する点に#があるかを判定すれば良い
int main(){
    int h, w;
    cin >> h >> w;
    int a[h][w];//input # is 0, . is 1
    for(int i=0;i < w;i++){
        for(int j=0;j < h;j++){
            char s;
            cin >> s;
            if(s == '#') a[i][j] = 0;
            else a[i][j] = 1;
        }
    }
    //境界条件の分岐って書くのがめんどくさい。簡単なやり方ないかな。。。
    //周囲の４つを調べて全て１ならbreak cout << "No" else そのままループ
    int tmp = 0;//posses condition if tmp == 1 cout "No"
    for(int i=0;i < w;i++){
        for(int j=0;j < h;j++){
            cout << i << " " << a[i][j] << j << endl;
            if(a[i][j] == 0 && (i-1 == -1 || a[i-1][j] == 1) && (i+1 == w || a[i+1][j] == 1) && (j-1 == -1 && a[i][j-1] == 1) && (j+1 == h || a[i][j+1] == 1)){
                tmp = 1;
                break;
            }
        if(tmp == 1) break;
        }
    }

    if(tmp ==1) cout << "No" << endl;
    else cout << "Yes" << endl;
    return 0;
}
