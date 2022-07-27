
def solution(n,m,arr):
	max_val = 0

	for i in range(n):
		arr[i].sort()
		if(arr[i][0] > max_val):
			max_val = arr[i][0]

	print(max_val)

	return max_val

	


n,m = map(int, input().split())

card = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
	tmp = input().split(" ")
	for j in range(len(tmp)):
		card[i][j] = int(tmp[j])


solution(n,m,card)

