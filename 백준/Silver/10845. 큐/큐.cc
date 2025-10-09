#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include<queue>
#include <sstream>
using namespace std;


int main() {
    queue<int> qu;
    int n;
    cin >> n;
    string str;
    for (int i = 0; i < n+1; i++) {
        if (!getline(cin, str)) break;
        stringstream ss(str);
        string fro;
        ss >> fro;
        if (fro == "push") {
            int x;
            ss >> x;
            qu.push(x);
        }
        else if (fro == "pop") {
            if (qu.empty()) {
                cout << -1 << endl;
            }
            else {
                cout << qu.front() << endl;
                qu.pop();
            }
        }
        else if (fro == "size") {
            cout << qu.size() << endl;
        }
        else if (fro == "empty") {
            if (qu.empty()) {
                cout << 1 << endl;
            }
            else {
                cout << 0 << endl;
            }
        }
        else if (fro == "front") {
            if (qu.empty()) {
                cout << -1 << endl;
            }
            else {
                cout << qu.front() << endl;
            }
        }
        else if (fro == "back") {
            if (qu.empty()) {
                cout << -1 << endl;
            }
            else {
                cout << qu.back() << endl;
            }
        }
    }
    return 0;
}
