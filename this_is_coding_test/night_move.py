
def solution(cur):
	dx = [2,2,-2,-2,-1,1,-1,1]
	dy = [1,-1,1,-1,2,2,-2,-2]
	answer = 0

	if (('c' <= cur[0] and cur[0] <= 'f') and
			('3' <= cur[1] and cur[1] <= '6')):
		print(6)
		return

	x = int(cur[1]) - int('1') + 1
	y = ord(cur[0]) - ord('a') + 1

	for i in range(8):
		if((0 >= x+dx[i] or x+dx[i] >= 8) or ( 0 >= y+dy[i]  or y+dy[i] >= 8)):
			continue
		else:
			answer += 1
	
	print(answer)
	return answer


cur = input()

solution(cur)
