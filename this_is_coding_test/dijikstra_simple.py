import sys

#긴 줄을 입력받기 위해 사용
input = sys.stdin.readline
#정수의 가장 큰 수 갈 수 없는 곳의 무한대를 표현 초기 거리는 모두 무한으로 표현
INF = int(1e9)
#노드와 간선 입력
n, m = map(int, input().split())

#시작 노드 입력
start = int(input())

#그래프 초기화
graph = [[] for i in range(n+1)]

#방문 체크 리스트 
visited = [False] * (n+1)
#거리 리스트
distance = [INF] * (n+1)

#노드, 간선 그래프 입력
for _ in range(m):
	#a->노드, b->연결된 노드, c->연결된 노드까지의 거리
	a,b,c = map(int,input().split())
	graph[a].append((b,c))

#연결된 노드중 거리가 가장 짧은 노드 찾기 짧은 노드 가 중복이라면 숫자가 낮은 노드 리턴
def get_smallest_node():
	min_value = INF
	index = 0
	for i in range(1,n+1):
		if distance[i] < min_value and not visited[i]:
			min_value = distance[i]
			index = i
	return index

#다익스트라 함수 시작이 1이라 가정
def dijkstra(start):
	#거리, 방문 초기화 시작거리는 본인의 거리기 때문에 0으로 초기화
	distance[start] = 0
	visited[start] = True

	#시작 노드와 연결된 노드 모두 등록
	for j in graph[start]:
		distance[j[0]] = j[1]

	#마지막 노드 를 제외한 n-1번 반복 (ex: 6개의 노드가 존재한다면, 마지막 노드는 모두 거리가 정해져있으므로 안돌아도 된다.)
	for i in range(n-1):
		#가장 거리가 짧은 노드 찾기
		now = get_smallest_node()
		#가장 짧은 노드 방문처리
		visited[now] = True

		#가장 짧은 노드와 연결된 노드들을 탐색하며 거리정보 업데이트
		for j in graph[now]:
			cost = distance[now] + j[1]
			if cost < distance[j[0]]:
				distance[j[0]] = cost 

dijkstra(start)

for i in range(1,n+1):
	if distance[i] == INF:
		print("INFINITY")
	else:
		print(distance[i])



