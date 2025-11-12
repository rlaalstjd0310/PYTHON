#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> v1;
int main() {
    int n;
    cin >> n;
    for (int i = 0; i <n; ++i) {
        int m;
        cin >> m;
        v1.push_back(m);
    }
    sort(v1.begin(), v1.end());
    for (int i = 0; i < n; ++i) {
        cout << v1[i] << endl;
    }
    return 0;
}