from collections import deque


def binary_search(arr,target,start,end):
	if(start > end):
		return None

	mid = (start+end) // 2

	if(arr[mid] == target):
		return mid
	
	if(arr[mid] < target):
		return binary_search(arr,target,mid+1,end)
	else:
		return binary_search(arr,target,start,mid-1)


array = [0 for i in range(1000001)]

n = int(input())
n_arr = list(map(int,input().split()))

m = int(input())
m_arr = list(map(int,input().split()))


for i in n_arr:
	array[i] = 1

for i in m_arr:
	if(array[i] == 1):
		print("yes",end = " ")
	else:
		print("no",end = " ")
print()


for i in m_arr:
	if(not binary_search(n_arr,i,0,len(n_arr)-1)):
		print("no" ,end=" ")
	else:
		print("yes" ,end=" ")






