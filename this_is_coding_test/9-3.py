from collections import deque
from distutils.errors import DistutilsInternalError
import heapq
import sys
from turtle import distance

input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())
graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for i in range(m):
	a,b,c = map(int, input().split())
	graph[a].append((b,c))

def dijikstra(start):
	heap = []

	distance[start] = 0
	heapq.heappush(heap,(0, start))

	while heap:
		dist, now = heapq.heappop(heap)

		if dist > distance[now]:
			continue

		for i in graph[now]:
			cost = distance[now] + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(heap,(cost, i[0]))

def main():
	dijikstra(start)

	count = 0
	maxtime = 0
	for i in range (1,n+1):
		if distance[i] != INF and distance[i] != 0:
			count += 1
			maxtime = max(maxtime, distance[i])

	print(count, maxtime)

if __name__ == '__main__':
	main()