from collections import deque
import heapq
import sys
import copy

INF = int(1e9)
input = sys.stdin.readline

n = int(input())

# 진입차수 
indegree = [0] * (n+1) 
time = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]:
        graph[j].append(i)
        indegree[i] += 1

# 진입차수가 0인 값 큐에 삽입

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

# 핵심 !! list를 복사할때는 깊은복사를 해야함
# 단순하게 넘겨주면 주솟값을 넘겨주는것과 같은 동작이 되어
# 원본도 값이 변경됨
result = copy.deepcopy(time)
#result = time

#위상정렬 실행
while q:
    node = q.popleft()

    for i in graph[node]:
        indegree[i] -= 1
        #예시에 나온경우는 차례대로 나오는 경우라 정상 동작하지만
        # 하나의 과목에 선수과목이 두가지 있는경우 동시 수강이 가능하므로
        # 가장 큰 값으로 넣어야됨
        result[i] = max(result[i], result[node]+time[i])
        if indegree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i])






        