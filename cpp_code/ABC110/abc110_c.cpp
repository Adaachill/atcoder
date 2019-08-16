#include <iostream>
#include <string>
using namespace std;

int main(){
	string S;
	string T;
	cin >> S >> T;
	int counter = 0;
	
	for(int i = 0;i < S.size(); i++){
		if(S[i] != T[i]){
			//prior i same character exist?
			//if so No
			for(int j = 0; j < i;j++){
				if(S[i] == S[j]){
					counter = 1;
					//1 means No
				}
			}
			//swap step
			S[i] = T[i];
			for(int k = i + 1;k < S.size();k++){
				if(S[i] == S[k]){
					if(S[k] != T[k]){
						counter = 1;
					}
					S[k] = T[k];
				}
			}
		}
	}
	
	if(counter == 0){
		cout << "Yes";
	}else cout << "No" << endl;
}

