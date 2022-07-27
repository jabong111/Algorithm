from collections import deque
import heapq
import sys
from tabnanny import check

INF = int(1e9)
input = sys.stdin.readline

#    u,d,l,r
dx = [-1,1,0,0]
dy = [0,0,-1,1]
global graph 
global checked
global n,m
#가로 세로

q = deque()

#가로(열), 세로(행)
m,n = map(int, input().split())
graph = [[] for _ in range(n)]
checked	= [[False] * m for _ in range(n)]

flag = False

for i in range(n):
	graph[i] = (list(map(int, input().split())))

for i in range(n):
	for j in range(m):
		if graph[i][j] == 1:
			q.append((i,j))
			checked[i][j] = True

def bfs():
	answer = 1

	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if (nx >= 0  and nx < n) and ( ny >= 0 and ny < m):
				if graph[nx][ny] == -1 or checked[nx][ny] or graph[nx][ny] == 1:
					continue
				else:
					q.append((nx,ny))
					checked[nx][ny] = True
					graph[nx][ny] = graph[x][y] + 1
					answer = max(answer, graph[nx][ny]) 
	return answer

answer = bfs()

for i in range(n):
	for j in range(m):
		if graph[i][j] == 0:
			flag = True

if flag:
	print(-1)
else:
	print(answer-1)