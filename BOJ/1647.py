from collections import deque
import grp
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b :
		parent[b] = a
	else:
		parent[a] = b

n,m = map(int, input().split())

parent = [0] * (n+1)

# 부모노드 초기화
for i in range(n+1):
	parent[i] = i

graph = []

for i in range(m):
	a, b, c = map(int, input().split()) 
	graph.append((c,a,b))

graph.sort()

answer = 0
max = 0

for i in graph:
	cost, a, b = i

	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a,b)
		answer += cost
		if cost >  max:
			max = cost


print(answer-max)






