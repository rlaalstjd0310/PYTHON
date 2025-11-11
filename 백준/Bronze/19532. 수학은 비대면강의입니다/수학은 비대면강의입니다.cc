#include <iostream>
#include <cassert>
#include <limits>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int a, b, c, d, e, f;
	cin >> a >> b >> c >> d >> e >> f;
	for (int i = -999; i < 1000; ++i) {
		for (int j = -999; j < 1000; ++j) {
			if (a * i + b * j == c) {
				if (d * i + e * j == f) {
					cout << i << " " << j;
				}
				else {
					continue;
				}
			}
			else {
				continue;
			}
		}
	}

	
	return 0;
}