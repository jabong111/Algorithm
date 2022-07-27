
def solution(n,arr):
	answer = 0
    #    r l u  d
	x = 1 
	y = 1
	dx = [0,0,1,-1]
	dy = [1,-1,0,0]
	
	for direction in arr:
		if direction == 'R':
			pos = 0
		elif direction == 'L':
			pos = 1
		elif direction == 'D':
			pos = 2
		elif direction == 'U':
			pos = 3

		if( x+dx[pos] <= 0  or y+dy[pos] <= 0):
			continue
		x = x+dx[pos]
		y = y+dy[pos]


	print(x,y)
	return answer


n =  int(input())
arr = list(input().split())

solution(n,arr)


