#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include<stack>
#include <sstream>
using namespace std;

int main() {
    stack<int> s;
    string str;

    while (getline(cin, str)) {
        if (str.empty()) {
            continue;
        }
        stringstream ss(str);
        string command;

        ss >> command;

        if (command == "push") {
            int value;
            if (ss >> value) {
                s.push(value);
            }
        }
        else if (command == "pop") {
            if (!s.empty()) {
                cout << s.top() << endl;
                s.pop();
            }
            else {
                cout << -1 << endl;
            }
        }
        else if (command == "top") {
            if (!s.empty()) {
                cout << s.top() << endl;
            }
            else {
                cout << -1 << endl;
            }
        }
        else if (command == "size") {
            cout << s.size() << endl;
        }
        else if (command == "empty") {
            cout << (s.empty() ? 1 : 0) << endl;
        }
    }

    return 0;
}
