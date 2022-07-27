from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n,m,k,x = map(int,input().split())

arr = [[] for _ in range(n+1)]

for i in range(m):
	a,b = map(int, input().split())
	arr[a].append(b)

bfs_check = [False] * (n+1) 
distance = [0] * (n+1)

def bfs(start):
	q = deque()
	q.append(start)
	bfs_check[start] = True

	while q:
		x = q.popleft()

		for i in arr[x]:
			if not bfs_check[i]:
				distance[i] = distance[x] + 1
				q.append(i)
				bfs_check[i] = True


bfs(x)

answer = []
for i in range(len(distance)):
	if distance[i] == k:
		answer.append(i)

if len(answer) == 0:
	print(-1)

for i in answer:
	print(i) 

