import sys
import heapq

input = sys.stdin.readline
#무한대를 위해 가장큰 int 
INF = int(1e9)

# 노드, 간선 입력
n,m = map(int,input().split())

#그래프 초기화
graph = [[] for _ in range(n+1)]

#priority queue를 사용하기 위해서 선언
#heapq.heappush(heap, (거리, 노드))
heap = []

#시작점 
start = int(input())

distance = [INF] * (n+1)
#방문처리는 안해도됨

for i in range(m):
	#간선, 연결된간선, 거리
	a,b,c = map(int,input().split())
	graph[a].append((b,c))

def dijikstra(start):
	distance[start] = 0
	heapq.heappush(heap,(distance[start], start))

	while heap:
		dist,now = heapq.heappop(heap) 
		#가장 짧은 거리의 노드가 현재 거리보다 크면 update가 필요없기 때문에 skip
		if dist > distance[now]:
			continue
 
		for i in graph[now]:
			cost = distance[now] + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(heap,(cost, i[0]))


def main():
	dijikstra(start)
	for i in range(1,n+1):
		if distance[i] == INF:
			print("INFINITY", end=" ")
		else:
			print(distance[i], end=" ")
	print()

	return 0


if __name__ == '__main__':
	main()
