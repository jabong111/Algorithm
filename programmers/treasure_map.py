
def solution(n,arr1,arr2):
	answer = []
	tmp_bin = []
	for idx in range(n):
		tmp = bin(arr1[idx] | arr2[idx])
		tmp_bin.append(str(tmp[2:]))

	for line in tmp_bin:
		print(line.zfill(n))
		#tmp1 = line.replace("1","#")
		#tmp2 = tmp1.replace("0"," ")
		#answer.append(tmp2)


	return answer

n = int(input())
arr1 = []
arr2 = []

tmp = input().split(" ")

for i in range(n):
	arr1.append(int(tmp[i]))

tmp = input().split(" ")

for i in range(n):
	arr2.append(int(tmp[i]))

solution(n,arr1,arr2)
