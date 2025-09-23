#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main() {
	string k;
	getline(cin, k);
	int count = 0;
	{
		if (k.front() == ' ') {
			--count;
		}
		else {
		}
	}
	{
		if (k.back() == ' ') {
			--count;
		}
		else {
		}
	}
	for (int i = 0; i < k.length(); ++i) {
		if (k.at(i) == ' ') {
			++count;
		}
		else {
			continue;
		}
	}
	cout << count+1;
}
