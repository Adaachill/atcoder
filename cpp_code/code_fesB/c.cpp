#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N;
    cin >> N;
    char a[N][N];
    int b[N][N];//bit map
    //fill all point with '.'
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            a[i][j] = '.';
            b[i][j] = 0;
        }
    }

    //fill upper edge 1,3,5...
    for(int i=0;i<N;i++){
        if((i%5)%2 == 1) a[0][i] = 'x';
        if((i%5) == 1){
            if(i-2>=0) a[1][i-2] = 'x';
            if(i+1<=N-1) a[2][i+1] = 'x';
        }
    }

   
    for(int i=1;i<N-1;i++){
        for(int j=0;j<N;j++){
            if(a[i][j] == 'x'){
                a[i][j] = a[i+1][j] = a[i-1][j]=a[i][j+1]=a[i][j-1] =1;
                //cout << i << ".." <<j<<".." << endl;/////
                if(j-2>=0) a[i+1][j-2] = 'x';
                if(j+1<=N-1) a[i+2][j+1] = 'x';
            }
        }
    }

    //edge 
    for(int i=1;i<N-1;i++){
        if(b[i][0] == 0){
            a[i][0] = 'x';
            b[i+1][0] = 1;
        }
    }
   for(int i=1;i<N-1;i++){
        if(b[i][0] == 0){
            a[i][0] = 'x';
            b[i+1][0] = 1;
        }
    }
   for(int i=0;i<N;i++){
        if(b[i][0] == 0){
            a[i][0] = 'x';
            b[i+1][0] = 1;
        }
    }
     
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cout << a[i][j];
        }
        cout << endl;
    }



    return 0;
}
