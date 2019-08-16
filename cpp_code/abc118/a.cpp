
#include <iostream>
using namespace std;

int main(){
	int a,b;
	cin >> a >> b ;

	//b%a == 0 then a+b else b-a

	if(b%a == 0){
		cout << a+b << endl;
    }else cout << b-a << endl;
}
