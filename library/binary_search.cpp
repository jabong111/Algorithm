#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

using namespace std;

typedef int		*A;
typedef struct _node *tree_pointer;

typedef struct _node{
	int data;
	tree_pointer left_child,right_child;
}node;


void preorder(tree_pointer ptr)
{
	if(ptr){
		cout << ptr->data << " ";
		preorder(ptr->left_child);
		preorder(ptr->right_child);
	}
}

void inorder(tree_pointer ptr)
{
	if(ptr){
		inorder(ptr->left_child);
		cout << ptr->data << " ";
		inorder(ptr->right_child);
	}

}

void postorder(tree_pointer ptr)
{
	if(ptr){
		postorder(ptr->left_child);
		postorder(ptr->right_child);
		cout << ptr->data << " ";
	}

}

void init_node(tree_pointer ptr, int size)
{
	int i;
	for(i=1;i<size;i++){
		ptr[i].data = i;
		ptr[i].left_child = NULL;
		ptr[i].right_child = NULL;
	}

}

int main()
{
	int i;
	int n = 15;
	node nodes[n+1];

	init_node(nodes, n+1);

	for(i=1;i<n+1;i++){
		if(i%2 == 0){
			nodes[i/2].left_child = &nodes[i];
		}else{
			nodes[i/2].right_child = &nodes[i];
		}
	}

	preorder(&nodes[1]);

	return 0;
}
