#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;
int memo[1001];
int d[1001];

int dynamic(int x)
{
	if(x == 1) return 1;
	if(x == 2) return 2;

	if(memo[x])
		return memo[x];

	return memo[x] = (dynamic(x-1) + dynamic(x-2)) % 10007;
}

int main()
{
	int n;
	cin >> n;

	cout << dynamic(n) << endl;

	return 0;
}
