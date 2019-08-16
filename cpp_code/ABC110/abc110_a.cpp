#include <iostream>
using namespace std;

int main(){
	int a,b,c;
	cin >> a >> b >> c;

	//find max
	int money;
	if(a > b && a > c){
		money = a * 10 + b + c;
	}else if(b > c){
		money = b * 10 + a + c;
	}else money = a + b + c * 10;

	cout << money;
}
