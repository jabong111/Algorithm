/*
   BFS Breath First Search (너비우선탐색)
   -> 탐색을 할 떄 너비를 우선으로 하여 탐색을 수행하는 탐색 알고리즘
   '맹목적인 탐색'을 하고자 할 떄 사용할 수 있는 탐색 기법. 
   *최단경로, 미로탐색 등* 
   준비물은 Queue

   1. 큐에서 하나의 노드를 꺼낸다.
   2. 해당 노드에 연결된 노드 중 방문하지 않은 노드를 방분하고, 차례대로 큐에 삽입.

		    1
		 /     \
		2   -	3	
	   / \     / \
	  4 - 5   6 - 7

	  1 -> 2,3
	  2 -> 1,3,4,5
	  3 -> 1,2,6,7
	  4 -> 2,5
	  5 -> 2,4
	  6 -> 3,7
	  7 -> 3,6
 */

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

int number = 7;
int checked[8];
vector<int> arr[8];

void bfs(int start)
{
	int i;
	queue<int> q;
	q.push(start);
	checked[start] = 1;

	while(!q.empty()){
		int x = q.front();
		q.pop();
		printf("%d ", x);

		for(i=0;i<arr[x].size();i++){
			int y = arr[x][i];
			if( !checked[y]){
				q.push(y);
				checked[y] = 1;
			}
		}
	}
}

int main()
{
	arr[1].push_back(2);
	arr[1].push_back(3);

	arr[2].push_back(1);
	arr[2].push_back(3);
	arr[2].push_back(4);
	arr[2].push_back(5);

	arr[3].push_back(1);
	arr[3].push_back(2);
	arr[3].push_back(6);
	arr[3].push_back(7);

	arr[4].push_back(2);
	arr[4].push_back(5);

	arr[5].push_back(2);
	arr[5].push_back(4);

	arr[6].push_back(3);
	arr[6].push_back(7);

	arr[7].push_back(3);
	arr[7].push_back(6);
	bfs(1);
	printf("\n");
	return 0;
}
