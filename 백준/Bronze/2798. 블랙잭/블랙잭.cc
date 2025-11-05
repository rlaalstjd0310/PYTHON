#include <iostream>
#include <cassert>
#include <limits>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int a = 0;
	int n, m;
	cin >> n >> m;

	vector<int> v1(n);
	for (int i = 0; i < n; ++i) {
		int k;
		cin >> v1[i];
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 1+i; j < n; ++j) {
			for (int k = j + 1; k < n; ++k) {
				int sum = v1[i] + v1[j] + v1[k];

				if (sum > m) {
					continue;
				}
				else {
					a = max(a, sum);
				}
			}

		}
	}
	cout << a << endl;

	return 0;
}