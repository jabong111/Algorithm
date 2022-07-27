
def binary_search(arr,target,start,end):
	while start <= end:
		mid = (start + end) // 2

		if(array[mid] == target):
			return mid
		
		if(array[mid] < target):
			start = mid+1
		else:
			end = mid-1

	return None


n, target =map(int,input().split())

array = list(map(int,input().split()))

idx = binary_search(array,target,0,n-1)

print(idx)
	





