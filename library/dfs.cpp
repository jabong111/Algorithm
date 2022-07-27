/*
   DFS Depth First Search (깊이우선탐색)
   깊은  것을 우선적으로 탐색하는 알고리즘
   맹목적으로 각 노드를 탐색할 때 주로 사용된다.
   준비물은 스택 (컴퓨터 기본구조가 스택이므로 스택이 없이 재귀함수만으로도 구현가능)

   1. 스택의 최상단 노드를 확인
   2. 최상단 노드에게 방문하지 않은 인접 노드가 있으면 그 노드를 스택에 넣고 방문처리
      방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 뺀다.

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

void dfs(int start)
{
	int i,y;
	int x = start;
	if(checked[x])
		return;

	checked[x] = 1;

	printf("%d ", x);
	for(i=0;i<arr[x].size();i++){
		y = arr[x][i];
		dfs(y);
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

	dfs(1);
	printf("\n");
	return 0;
}
