#include <iostream>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;

int main(){
    int n, m;
    int count = 0;
    cin >> n >> m;
    if (m % 2 != 0) {
        for (int i = 0; i < n; ++i) {
            int o = 0;
            int x = 0;
            string k;
            cin >> k;
            for (int j = 0; j < m; ++j) {
                if (k[j] == 'O') {
                    o++;
                }
                else if (k[j] == 'X') {
                    x++;
                }
            }
            if (o > x) {
                count++;
            }
        }
        cout << count;
    }
    return 0;
}