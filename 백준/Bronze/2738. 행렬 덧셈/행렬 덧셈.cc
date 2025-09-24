#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;


int main() {
	int n, m;
	cin >> n >> m;
	vector <vector<int>> v1(n, vector<int>(m));
	for (int i = 0; i < v1.size(); ++i) {
		for (int j = 0; j < v1[i].size(); ++j) {
			int a;
			cin >> v1[i][j];
		}	
	}
	vector <vector<int>> v2(n, vector<int>(m));
	for (int i = 0; i < v2.size(); ++i) {
		for (int j = 0; j < v2[i].size(); ++j) {
			int a;
			cin >> v2[i][j];
		}
	}
	for (int i = 0; i < v1.size(); ++i) {
		for (int j = 0; j < v1[i].size(); ++j) {
			cout << v1[i][j] + v2[i][j] << " ";
		}
		cout << "\n";
	}
	return 0;
}