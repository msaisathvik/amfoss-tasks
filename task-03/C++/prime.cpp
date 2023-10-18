#include <iostream>
using namespace std;
int main() {
    int x;
    cout << "Enter a number: ";
    cin >> x;
    for (int i=2;i<x+1;i++){
        int count = 0;
        for (int j=1;j<i+1;j++){
            if (i%j==0) count++;
        }
        if (count == 2) cout << i << " ";
    }
    return 0;
}