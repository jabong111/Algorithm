
		
n = int(input())
arr = []
for i in range(n):
	arr.append((int(input())))


answer = sorted(arr, reverse=True)

for i in range(n):
	print(answer[i], end=" ")
		
