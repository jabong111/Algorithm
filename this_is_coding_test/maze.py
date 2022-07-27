from collections import deque

#    u d  l r
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())
checked = [[0] * m for i in range(n)]

array = []
for i in range(n):
	array.append(list(map(int,input())))

def bfs(x,y):
	q = deque()
	q.append((x,y))
	checked[x][y] = 1

	while q:
		x,y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if((nx >= 0 and nx < n) and ( ny >= 0 and ny < m) and (not checked[nx][ny]) and (array[nx][ny] == 1)):
				array[nx][ny] += array[x][y]
				checked[nx][ny] = 1
				q.append((nx,ny))

bfs(0,0)

for i in range(n):
	print(array[i])

answer = array[n-1][m-1]

print(answer)





