
def binary_search(array,target,start,end):
	if(start > end):
		return None

	mid = (start + end) // 2

	if(array[mid] == target):
		return mid
		
	#왼쪽에 있으면 왼쪽 탐색
	if(array[mid] > target):
		return binary_search(array,target,start,mid-1)
	#오른쪽에 있으면 오른쪽 탐색
	else:
		return binary_search(array,target,mid+1,end)
	
n, target =map(int,input().split())

array = list(map(int,input().split()))

idx = binary_search(array,target,0,n-1)

print(idx)
	





