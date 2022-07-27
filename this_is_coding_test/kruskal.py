from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

def find_parent(parent,x):
	#부모노드 찾기
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent,a,b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b:
		parent[b] = a
	else:
		parent[a] = b

# 노드 ,간선 입력
node, edge = map(int, input().split())
answer = 0

graph = []  
parent = [0] * (node+1)

# 부모노드 를 본인 노드로 초기화
for i in range(1,node+1):
	parent[i] = i 

#그래프 정보 입력 받기
for i in range(edge):
	# (a,b) -> 그래프  c -> cost
	a,b,c = map(int, input().split())
	graph.append((c,a,b))

graph.sort()

for gr in graph:
	cost, a, b = gr
	if find_parent(parent,a) != find_parent(parent,b):
		union_parent(parent,a,b)
		answer += cost

print(answer)
print(parent)


	




