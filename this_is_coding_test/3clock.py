
def solution(n):
	answer = 0
	for time in range(n+1):
		for minute in range(60):
			for second in range(60):
				time = str(time)
				minute = str(minute)
				second = str(second)
				if(time.find('3') != -1 or minute.find('3') != -1 or second.find('3') != -1):
#if '3' in time+minute+second:
					answer += 1
	print(answer)
	return answer


n = int(input())

solution(n)
