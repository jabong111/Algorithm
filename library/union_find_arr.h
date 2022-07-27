#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>

void init_parent(int* parent);
int get_parent(int* parent, int x);
void union_parent(int* parent, int x, int y);
int find_parent(int* parent, int x, int y);
