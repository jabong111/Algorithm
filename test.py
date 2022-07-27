from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

# board size 
n = int(input())

board = [[0] * n for _ in range(n)]

# apple
k = int(input())

#사과의 위치를 1로 표시
for i in range(k):
    a,b = map(int, input().split())
    board[a-1][b-1] = 1 

#방향
l = int(input())

directions = []
for i in range(l):
    a,b = input().split()
    directions.append((int(a),b))

#    동 남 서 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def get_direction(current, direction):
    if direction == 'D':
        current = (current+1) % 4
    elif direction == 'L':
        current = (current-1) % 4
    return current

def simulation():
    # 뱀의 위치들 포함
    q = deque()
    #뱀의 시작 위치
    x,y = 0,0
    q.append((x,y))
    current = 0 #동쪽 부터 시작
    timer = 0   #시간측정

    while True:
        nx = x + dx[current]
        ny = y + dy[current]

        if nx >= n or ny >= n:
            return timer + 1

        if nx < 0 or ny < 0:
            return timer + 1

        if board[nx][ny] == 2:
            return timer + 1

            #사과가 있는지 확인
        if board[nx][ny] == 1:  #사과가 있으면 위치 추가
            board[nx][ny] = 2
            q.append((nx,ny))
        else:                   #사과가 없으면 꼬리 제거
            board[nx][ny] = 2
            q.append((nx,ny))
            tx,ty = q.popleft()
            board[tx][ty] = 0

        x,y = nx,ny
        timer += 1

        #방향 전환 했는지 확인
        for which in directions:
            if which[0] == timer:
                current = get_direction(current,which[1])


print(simulation())
