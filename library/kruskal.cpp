#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

typedef struct edge{
	int node[2];
	int distance;
}Edge;

Edge init_struct(int node1,int node2, int distance)
{
	Edge edge;
	edge.node[0] = node1;
	edge.node[1] = node2;
	edge.distance = distance;

	return edge;
}

bool compare (Edge edge1, Edge edge2)
{
	return edge1.distance < edge2.distance;
}

void init_parent(int* parent,int size){
	int i;
	for(i=0;i<size;i++){
		parent[i] = i;
	}

}

int get_parent(int* parent, int x){

	if(parent[x] == x)
		return x;

	return parent[x] = get_parent(parent,parent[x]);
}


void union_parent(int* parent, int x, int y){
	x = get_parent(parent, x);
	y = get_parent(parent, y);

	if(x < y)
		parent[y] = x;
	else
		parent[x] = y;
}


int find_parent(int* parent, int x, int y){
	x = get_parent(parent, x);
	y = get_parent(parent, y);

	if (x==y)
		return 1;

	return 0;
}

int main()
{
	int i;
	int n=7;	//노드
	int m=11;   //간선
	int sum = 0; //최소 간선의 합
	int parent[n+1];

	Edge e;
	vector<Edge> v;

	v.push_back(init_struct(1,7,12));
	v.push_back(init_struct(1,4,28));
	v.push_back(init_struct(1,2,67));
	v.push_back(init_struct(1,5,17));
	v.push_back(init_struct(2,4,24));
	v.push_back(init_struct(2,5,62));
	v.push_back(init_struct(3,5,20));
	v.push_back(init_struct(3,6,37));
	v.push_back(init_struct(4,7,13));
	v.push_back(init_struct(5,6,45));
	v.push_back(init_struct(5,7,73));

	//간선의 거리를 오름차순으로 정렬
	sort(v.begin(), v.end(),compare);

	//parent 초기화
	init_parent(parent,n+1);

	for(i=0;i<v.size();i++){

		//cycle 확인
		if(find_parent(parent,v[i].node[0], v[i].node[1]))
			continue;

		union_parent(parent, v[i].node[0], v[i].node[1]);
		sum += v[i].distance;
	}



	cout << sum << endl;


	return 0;
}
