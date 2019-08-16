#include <iostream>
#include <string>
using namespace std;

int main(){
  string s;
  cin >> s;
  int count = 0;
  int start = 0;
  int a[3];
  for(int i=0;i < s.size();i++){
    if(s[i] == '/'){
        a[count] = atoi((s.substr(start+1,i-start)).c_str());
        start = i;
        count++;
    } 
  }
  //cout << a[1];
  if(a[1] <5) cout << "Heisei";
  else cout << "TBD";
  return 0;
}