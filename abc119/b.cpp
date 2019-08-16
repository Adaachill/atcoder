#include <iostream>
#include <string>
using namespace std;

int main(){
  int N;
  cin >> N;
  double x[N];
  string u[N];
  double sum = 0;
  for(int i=0;i<N;i++){
    cin >> x[i] >> u[i];
    if(u[i] == "JPY") sum += x[i];
    else sum += x[i]*380000.0;
  }
  cout << sum << endl;
  return 0;
}