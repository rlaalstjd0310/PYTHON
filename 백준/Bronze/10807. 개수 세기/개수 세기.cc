#include<iostream>
#include<string>
using namespace std;

int main() {
	int n;
	int nums[101];
	cin >> n;

	for (int i = 0; i < n; ++i) {
		cin >> nums[i];
	}

	int m;
	cin >> m;

	int count = 0;
	for (int i = 0; i < n; ++i) {
		if (m == nums[i]) {
			count++;
		}
	}
	cout << count;
	return 0;
}