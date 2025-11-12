#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;

int arr[10001] = { 0 };

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        int m;
        cin >> m;
        arr[m-1]++;
    }
    for (int i = 0; i < 10000; ++i) {
        for (int j = 0; j < arr[i]; ++j) {
            cout << i+1 << "\n";
        }
    }
    return 0;
}