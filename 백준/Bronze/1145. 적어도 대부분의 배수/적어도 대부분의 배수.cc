#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> v1;
int main() {
	for (int i = 0; i < 5; ++i) {
		int n;
		cin >> n;
		v1.push_back(n);
	}
	int current = 1;
	while (true) {
		int count = 0;
		for (int i = 0; i < 5; ++i) {
			if (current % v1[i] == 0) {
				count ++;
			}
		}
		if (count >= 3) {
			cout << current << endl;
			break;
		}
		current++;
	}
	return 0;
}