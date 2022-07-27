def rotate(direction):
	ret = direction - 1
	if(ret < 0):
		ret = 3
	return ret

def backward(direction):
	if(direction < 2):
		ret = direction + 2
	else:
		ret = direction - 2
	return ret
#1. 왼쪽 방향 -> dy[direction-1]dx[direction-1]
#2. 왼쪽방향으로 회전 -> direction - 1 
#    				0 - 1 -> 3
#3. 바라보는 방향을 유지한태로 한칸 뒤로 ->  북  : 남쪽으로 한칸이동
#									    동  : 서쪽으로 한칸이동
#										남  : 북쪽으로 한칸이동
#										서  : 동쪽으로 한칸이동

n, m = map(int, input().split())

#방문처리를 위한 tmp맵
d = [[0] * m for i in range(n)]

x,y,direction = map(int, input().split())

d[x][y] = 1

#지도를 만듬
array = []
for i in range(n):
	array.append(list(map(int, input().split())))

#     북 동 남 서
#     0  1 2  3
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def solution(x,y,direction,n,m):
	answer = 1
	cur = 0
	while True:
		flag = 0
		for i in range(4):
			cur = direction
			direction = rotate(direction)

			nx = x + dx[direction]
			ny = y + dy[direction]
			if(nx < 0 or nx >= n):
				continue
			if(ny < 0 or ny >= m):
				continue

			if(d[nx][ny] != 0 or array[nx][ny] != 0):
				continue
			elif(d[nx][ny] == 0 and array[nx][ny] == 0):
				answer += 1
				d[nx][ny] = 1
				# 이동한 위치로 현재 위치 변경
				x = nx
				y = ny
				flag = 1
				break
		if(flag == 0):
			back = backward(direction)
			x = x + dx[back]
			y = y + dy[back]
			if(array[x][y] == 1): #바다면
				break
	print(answer)


solution(x,y,direction,n,m)
#   0 1 2 3
#0	1 1 1 1    0 0 0 0
#1	1 0 0 1    0 1 1 0
#2	1 1 0 1    0 0 1 0
#3	1 1 1 1    0 0 0 0
#map 크기 지정
