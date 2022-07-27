#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;


int main()
{
	int dp[1001];
	int n;
	int i;

	dp[1] = 1;
	dp[2] = 3;

	cin >> n;

	for(i=3;i<=n;i++){
		dp[i] = (dp[i-1] + (2*dp[i-2])) % 10007;
	}

	cout << dp[n] << endl;
	return 0;
}
