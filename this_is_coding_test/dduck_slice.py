n,m = map(int,input().split())

arr = list(map(int,input().split()))

def binary_search(target,start,end):
	if(start > end):
		return None
	
	mid = (start + end) // 2

	total = 0
	for x in arr:
		if x > mid:
			total += (x-mid)

	if(total == target):
		return mid
	
	if(total > target):
		return binary_search(target,mid+1, end)
	else:
		return binary_search(target,start, mid-1)

#answer = binary_search(m,0,19)

start = 0
end = max(arr) 
target = m
answer = 0

while start <= end:
	mid = (start + end) // 2

	total = 0
	for x in arr:
		if x > mid:
			total += (x-mid)

	if total >= target : 
		answer = mid
		start = mid + 1
	else:
		end = mid-1


print(answer,end="\n")

		





