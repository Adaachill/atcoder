#include <iostream>
#include <vector>

using namespace std;

int main(){
	int N,M,X,Y;
	cin >> N >> M >> X >> Y;
	int x[100];
	int y[100];
	int x_max = X;
	int y_min = Y;

	for(int i = 0;i < N; i++){
		//int x[i];
		cin >> x[i];
		if(x_max < x[i]) x_max = x[i];
	}
	for(int j = 0;j < M;j++){
		cin >> y[j];
		if(y_min > y[j]) y_min = y[j];
	}
	
	if(y_min <= x_max){
		cout << "War" << endl;
	}else{
		cout << "No War" << endl;
	}
	
	//debug
	//cout << x_max << y_min << endl;
}

