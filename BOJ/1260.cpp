#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

int visited[1001];
vector<int> arr[1001];

void init_visited(void)
{
	int i;
	for(i=0;i<1001;i++){
		visited[i] = 0;
	}
}

void bfs(int start)
{
	int i,x,y;
	queue<int> q;
	visited[start] = 1;
	q.push(start);

	while(!q.empty()){
		x = q.front();
		q.pop();
		printf("%d ",x);
		for(i = 0;i<arr[x].size();i++){
			y = arr[x][i];
			if(!visited[y]){
				visited[y] = 1;
				q.push(y);
			}
		}
	}
}

void dfs(int x)
{
	int i,y;
	if(visited[x])
		return;

	visited[x] = 1;
	printf("%d ",x);

	for(i=0;i<arr[x].size();i++){
		y = arr[x][i];
		dfs(y);
	}


}

int main()
{
	int i,j;
	int n,m,v;
	int a, b;
	cin >> n >> m >> v;

	for(i=0;i<m;i++){
		cin >> a >> b;
		arr[a].push_back(b);
		arr[b].push_back(a);
	}

	for(i=0;i<n;i++){
		sort(arr[i+1].begin(),arr[i+1].end());
#if 0
		for(j=0;j<arr[i+1].size();j++){
			printf("%d ",arr[i+1][j]);
		}
		printf("\n");
#endif
	}

	dfs(v);
	cout<<endl;
	init_visited();

	bfs(v);
	cout<<endl;
	return 0;
}
