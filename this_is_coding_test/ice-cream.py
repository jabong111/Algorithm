
from collections import deque


n,m = map(int,input().split())

array = []
for i in range(n):
	array.append(list(map(int,input())))

#     u d l r
dx = [-1,1,0,0]
dy = [0,0,-1,1]

checked = [[0] * m for i in range(n)]

def bfs(x,y):
	q = deque()
	q.append((x,y))
	checked[x][y] = 1

	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if ((nx >= 0 and nx < n) and (ny >= 0 and ny < m ) and (array[nx][ny] == 0 and checked[nx][ny] == 0)):
				q.append((nx,ny))
				checked[nx][ny] = 1


answer = 0
for i in range(n):
	for j in range(m):
		if((not array[i][j]) and  (not checked[i][j])):
			bfs(i,j)
			answer += 1

print(answer)

