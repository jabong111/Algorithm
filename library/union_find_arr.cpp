#include "union_find_arr.h"

using namespace std;


void init_parent(int* parent){
	int i;
	for(i=0;i<9;i++){
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
	int parent[9];
	int i;

	init_parent(parent);

	union_parent(parent,1,2);
	union_parent(parent,2,3);
	union_parent(parent,3,4);

	union_parent(parent,5,6);
	union_parent(parent,6,7);
	union_parent(parent,6,8);

	for(i=1;i<9;i++){
		cout << parent[i] << " ";
	}
		cout << endl;

	return 0;
}
