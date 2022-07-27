#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

int n,m;

int visit[101][101];
int maze[101][101];

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};

void bfs(pair<int, int> start){
	int i;
	int mx,my;
	int sum = 1;
	pair<int,int> x;
	queue< pair<int,int> > q;
	q.push(start);
	visit[start.first][start.second] = 1;

	while(!q.empty()){
		x = q.front();
		q.pop();
		sum = maze[x.first][x.second];
		for(i=0;i<4;i++){
			mx = x.first + dx[i];
			my = x.second + dy[i];
			if((0 < mx && mx <= n) && (0< my && my <= m)){
				if(maze[mx][my] && !visit[mx][my]){
					q.push(make_pair(mx,my));
					visit[mx][my] = 1;
					maze[mx][my] += sum;
				}
			}
		}
	}
}

int main()
{
	int i,j,k;

	cin >> n >> m;

	for(i=1;i<=n;i++){
		for(j=1;j<=m;j++){
			scanf("%1d",&maze[i][j]);
		}
	}

	bfs(make_pair(1,1));

	cout << maze[n][m];

	return 0;
}
