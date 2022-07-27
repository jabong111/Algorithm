from collections import deque

array = [ 
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7],
] 

dfs_check = [False] * 9
bfs_check = [False] * 9

def dfs(start):
	if(dfs_check[start] == True):
		return

	dfs_check[start] = True
	print(start ,end=" ")

	for i in array[start]:
		 dfs(i)


def bfs(start):
	q = deque()
	q.append(start)
	bfs_check[start] = True

	while q:
		x = q.popleft()
		print(x , end=" ")

		for i in array[x]:
			if not bfs_check[i]:
				q.append(i)
				bfs_check[i] = True

#			if(bfs_check[i] == True):
#				continue
#			q.append(i)
#			bfs_check[i] = True

dfs(1)
print()
bfs(1)
