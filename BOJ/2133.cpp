#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

int d[31];

int dp(int x)
{
	if(x == 0)
		return 1;
	if(x == 1)
		return 0;
	if(x == 2)
		return 3;
	//memoization
	if(d[x] != 0) 
		return d[x];

	int i;
	int result = dp(x-2)*3;
	for(i=4; i<=x;i++){
		if(i % 2 == 0)
			result += dp(x-i)*2;
	}

	d[x] = result;
	return d[x];

}

int main()
{
	int n;
	cin >> n;

	cout << dp(n) << endl;



}
