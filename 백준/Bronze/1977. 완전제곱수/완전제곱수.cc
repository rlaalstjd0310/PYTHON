#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> v1;
int sum = 0;
int main() {
	int m, n;
	cin >> m;
	cin >> n;
	for (int i = 0; i <= 10000; ++i) {
		if ((i * i) >= m && (i * i) <= n) {
			v1.push_back(i * i);
		}
	}
	for (int i = 0; i < v1.size(); ++i) {
		sum += v1[i];
	}
	if (!v1.empty()) {
		cout << sum << endl;
		cout << v1[0];
	}
	else {	
		cout << "-1";
	}
	return 0;
}