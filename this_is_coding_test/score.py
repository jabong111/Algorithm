
#def solution(data):
#	return data[1]


n  = int(input())
arr = []
for i in range(n):
	arr.append(tuple(input().split()))

#answer = sorted(arr,key=solution)
answer = sorted(arr,key=lambda solution: solution[1])

for i in range(n):
	print(answer[i][0], end=" ")

