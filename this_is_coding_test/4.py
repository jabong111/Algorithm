
def solution(n,k):
	answer = 0

	while (n != 1):
		if(n%k == 0):
			n /= k
			answer += 1
		elif(n%k != 0):
			n -=  1
			answer += 1

	return answer



n,k = map(int,input().split())

print(solution(n,k))
