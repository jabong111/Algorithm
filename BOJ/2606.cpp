#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

int visit[101];
vector<int> a[101];
int virus;

void  dfs(int x)
{
	int i;
	int y;
	//방문 했으면 return
	if(visit[x])
		return;
	visit[x] = 1;
	virus++;

	for(i=0;i<a[x].size();i++){
		y = a[x][i];
		dfs(y);
	}

}

int main()
{
	int i;
	int n,m;
	int c1,c2;

	cin >> n;
	cin >> m;

	for(i=0;i<m;i++){
		cin >> c1 >> c2;
		a[c1].push_back(c2);
		a[c2].push_back(c1);
	}

	dfs(1);

	cout << virus-1 << endl;

	

	return 0;
}
