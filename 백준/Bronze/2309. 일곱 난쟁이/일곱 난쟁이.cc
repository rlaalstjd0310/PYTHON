#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> v1;
int sum = 0;
int main() {
	for(int i=0;i<9;++i){
		int n;
		cin >> n;
		v1.push_back(n);
	}
	for (int i = 0; i < v1.size(); ++i) {
		sum += v1[i];
	}
	bool found = false;
	for (int i = 0; i < v1.size() && !found; ++i) {
		for (int j = i+1; j < v1.size(); ++j) {
			if (v1[i]+v1[j]==sum-100) {
				v1.erase(v1.begin() + j);
				v1.erase(v1.begin() + i);
				found = true;
			}
		}
	}
	sort(v1.begin(), v1.end());
	for (int i = 0; i < v1.size(); ++i) {
		cout << v1[i] << endl;
	}
	return 0;
}