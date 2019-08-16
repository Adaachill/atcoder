#include <iostream>
#include <vector>
using namespace std;
//1..Nで全てが一致するものの個数を答える
//残っているものをリストに保持してそれを順番に検索する
int main(){
  int N,M;
  cin >> N >> M;
  int k[N];
  vector<int> fav;
  int match[M];
  for(int i = 0;i< N;i++){
    cin >> k[i];
    int a[k[i]];
    for(int j = 0;j<k[i];j++){
      cin >> a[j];
      if(i == 0) fav.push_back(a[j]);
      else {
        for(int k=0;k<fav.size();k++){
          if(fav[k] == a[j]){
            match[k] = 1;
            break;
          }
        }
      }
    }
    if(i != 0){
      for(int k=0;k<fav.size();k++){
        if(match[k] != 1) fav[k] = 0;
      }
    } 
  }
  int count = 0; 
  for(int k=0;k<fav.size();k++){
      if(fav[k] > 0) count++;
  }
  cout << count << endl;
  return 0;
  
}