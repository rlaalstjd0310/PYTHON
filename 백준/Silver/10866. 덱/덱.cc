#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include<deque>
#include <sstream>
using namespace std;


int main() {
    deque<int> dq;
    int n;
    cin >> n;
    string str;
    for (int i = 0; i < n+1; i++) {
        if (!getline(cin, str)) break;
        stringstream ss(str);
        string fro;
        ss >> fro;
        if (fro == "push_front") {
            int x;
            ss >> x;
            dq.push_front(x);
        }
        else if (fro == "push_back") {
            int x;
            ss >> x;
            dq.push_back(x);
        }
        else if (fro == "pop_front") {
            if (dq.empty()) {
                cout << -1 << endl;
            }
            else {
                cout << dq.front() << endl;
                dq.pop_front();
            }
        }
        else if (fro == "pop_back") {
            if (dq.empty()) {
                cout << -1 << endl;
            }
            else {
                cout << dq.back() << endl;
                dq.pop_back();
            }
        }
        else if (fro == "size") {
            cout << dq.size() << endl;
        }
        else if (fro == "empty") {
            if (dq.empty()) {
                cout << 1 << endl;
            }
            else {
                cout << 0 << endl;
            }
        }
        else if (fro == "front") {
            if (dq.empty()) {
                cout << -1 << endl;
            }
            else {
                cout << dq.front() << endl;
            }
        }
        else if (fro == "back") {
            if (dq.empty()) {
                cout << -1 << endl;
            }
            else {
                cout << dq.back() << endl;
            }
        }
    }
    return 0;
}
