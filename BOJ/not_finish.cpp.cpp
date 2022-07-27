#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>
#include <memory.h>

using namespace std;

int graph[101][101];
int origin[101][101];
int visit[101][101];

int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0};
int n;
int current_way;
int max_way; 

void init_graph()
{
	memset(visit, 0, sizeof(visit));
}

void dfs(int x, int  y, int height)
{
	int i;
	int mx, my;
	if(visit[x][y])
		return;

	visit[x][y] = 1;

	for(i=0;i<4;i++){
		mx = x + dx[i]; 
		my = y + dy[i];  
		if((1 <= mx && mx  <= n) && (1 <= my && my <= n) && graph[mx][my] > height)
			dfs(mx, my, height);
	}

}

int main()
{
	int i,j,height;
	cin >> n;
	int max = 1,min = 100;

	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			scanf("%1d",&graph[i][j]);
			if(max <= graph[i][j])
				max = graph[i][j];
			if(min >= graph[i][j])
				min  = graph[i][j];
		}
	}

	for(height=0;height<=max;height++){
		for(i=1;i<=n;i++){
			for(j=1;j<=n;j++){
				if(height < graph[i][j] && !visit[i][j]){
					dfs(i,j,height);
					current_way++;
				}
			}
		}
		if(current_way > max_way)
			max_way = current_way;
		current_way = 0;
		//visit 초기화 하기
		init_graph();
	}
	cout << max_way << endl;

	return 0;
}
