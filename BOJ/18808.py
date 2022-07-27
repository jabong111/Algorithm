from collections import deque
import heapq
import sys

INF = int(1e9)
intput = sys.stdin.readline

def rotate_sicker(sticker):
	#행 열
	r,c = len(sticker), len(sticker[0])

	#  행 -> 열, 열 -> 행
	n_r, n_c = c, r
	rotate_s = [[0] * n_c for _ in range(n_r)]
	for i in range(r):
		for j in range(c): # 5
			rotate_s[j][r - 1 -i] = sticker[i][j]

	return rotate_s 

def is_attachable(notebook,x,y,r,c,s):

	for i in range(r):
		for j in range(c):
			#스티커가 1인데 이미 값이 있으면 못붙임..
			if s[i][j] and notebook[x+i][y+j]:
				return 0
	#붙일 수 있음
	return 1


def attatch(notebook,x,y,r,c,s):

	for i in range(r):
		for j in range(c):
			if notebook[x+i][y+j] == 0:
				notebook[x+i][y+j] = s[i][j]

	return notebook

if __name__ == '__main__':

	answer = 0
	#노트북 행,열 스티커 개수
	n,m,k = map(int, input().split())

	#노트북 크기 초기화
	notebook = [[0] * m for _ in range(n)]

	#스티커 초기화 스티커 정보는 딕셔너리로
	sticker = [{} for _ in range(k)]

	#스티커 정보
	for i in range(k):
		#행 열
		r,c = map(int, input().split())
		sticker[i]['r'], sticker[i]['c'] = r,c
		sticker[i]['s'] = [list(map(int, input().split())) for _ in range(r)]
	

	# 스티커 개수만큼 돌아
	for i in range(k):
		r,c = sticker[i]['r'],sticker[i]['c']
		s = sticker[i]['s']
		attach_flag = False
		count = 0

		while count < 4:
			#사이즈가 안맞으면 방향 바꾸기
			if r > n or c > m:
				r, c = c, r
				s = rotate_sicker(s)
				count += 1
				continue

			#붙일 수 있는지 확인
			for i in range(n):
				if attach_flag:
					break
				for j in range(m):
					if i+r <= n and j+c <= m :
						if not is_attachable(notebook,i,j,r,c,s):
							continue
						else:
							#붙임
							notebook = attatch(notebook,i,j,r,c,s)
							attach_flag = True
							break

			if attach_flag:
				break

			r,c = c,r
			s = rotate_sicker(s)
			count += 1

	for i in range(n):
#		print(notebook[i])
		for j in range(m):
			if notebook[i][j] == 1:
				answer += 1
	print(answer)
		

		

 
