#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

int dp[1000001];

int main()
{
	int i,j;
	int n;
	int result;
	cin >> n;

	dp[0] = 1;
	dp[1] = 2;
	dp[2] = 7;

	for(i=3;i<=n;i++){
		result = (dp[i-1]*2 + dp[i-2]*3 + 2)  % 1000000007;
		for(j=3; j<=i ;j++){
			if( j%2 == 0){
				result += (2*dp[i-j]) % 1000000007;
			}
		}
		dp[i] = result;
	}


	cout << dp[n] << endl;

	return 0;
}
