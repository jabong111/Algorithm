from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

result = 0 #만들 수 있는 그룹
count = 0

data.sort()

for i in data:
    count += 1 #그룹원 추가
    if count >= i:
        result += 1 #그룹 카운팅
        count = 0  # 새로운 그룹원을 위해 초기화

print(result)


