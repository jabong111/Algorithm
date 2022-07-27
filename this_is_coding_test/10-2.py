from collections import deque
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

n, m = map(int, input().split())

# 부모노드 초기화
parent = [0] * (n+1)

for i in range(n+1):
	parent[i] = i

answer = []
for i in range(m):
	s,a,b = map(int, input().split())

	# 같은팀으로 합치기
	if s == 0:
		union_parent(parent, a,b)
	# 같은 팀 여부 확인
	else:
		if find_parent(parent, a) == find_parent(parent, b):
			answer.append("YES")
		else:
			answer.append("NO")


for i in answer:
	print(i)
