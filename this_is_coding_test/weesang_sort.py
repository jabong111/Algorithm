from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline


v,e = map(int, input().split())

#큐 생성
q = deque()

# 진입차수 초기화
indegree = [0] * (v+1)

graph = [[] for _ in range(v+1)]

for i in range(e):
	a,b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1

"""
#진입차수를 초기화 시킨다.
for i in range(v+1):
	for j in graph[i]:
		indegree[j] += 1
"""

#시작을 위해 진입차수가 0인 노드를 큐에 추가
for i in range(1,v+1):
	if indegree[i] == 0:
		q.append(i)

while q:
	a = q.popleft()
	print(a, end=" ")

	#연결된 노드들의 진입차수를 줄인다
	for i in graph[a]:
		indegree[i] -= 1
		if indegree[i] == 0:
			q.append(i)
	
print()



