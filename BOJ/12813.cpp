#include <iostream>
#include <string>
#include <bitset>
#include <algorithm>
using namespace std;
int main() {
    string s1,s2;
    cin >> s1 >> s2;
    bitset<10> a(s1),b(s2);
    cout << (a & b) << '\n';
    cout << (a | b) << '\n';
    cout << (a ^ b) << '\n';
    cout << (~a) << '\n';
    cout << (~b) << '\n';
    return 0;
}
