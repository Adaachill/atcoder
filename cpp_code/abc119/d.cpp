#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;

int main(){
  int a,b,q;
  cin >> a >> b >> q;
  long long s[a],t[b],res[q];
  int x[q];
  for(int i=0;i<a;i++){
    cin >> s[i];
  }
  for(int i=0;i<b;i++){
    cin >> t[i];
  }
  for(int i=0;i<q;i++){
    cin >> x[i];
    long long mins,mint,min2s,min2t;
    int s1,s2,t1,t2;
    mins = s[a];
    mint = t[b];//max
    for(int j=0;j<a;j++){
      if(mins > abs(s[j] - x[i])){
        mins = abs(s[j] - x[i]);
        s1 = j;
      }
    }
    for(int j=0;j<b;j++){
      if(mins > abs(t[j] - x[i])){
        mins = abs(t[j] - x[i]);
        t1 = j;
      }
    }
    min2s = min(abs(s[s1-1] - x[i]),abs(s[s1+1] - x[i]));
    min2t = min(abs(t[t1-1] - x[i]),abs(t[t1+1] - x[i]));
    if(abs(s[s1] - x[i])*abs(s[t1] - x[i])>0) res[i] = max(mins,mint);
    else res[i] = max(2*min(mins,mint)+max(mins,mint),min(min2s,min2t));
    
  }
  for(int i=0;i<q;i++){
    cout << res[i] << endl;
  }
  return 0;
}