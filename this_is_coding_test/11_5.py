from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())

datas = list(map(int, input().split()))

result = 0

weight = [0] * 11

# 무게별로 수 정하기
for data in datas:
    weight[data] += 1

for i in range(1,m+1):
    n -= weight[i] # A가 선택되지 않는 갯수
    result += (weight[i] * n) #A가 선택 할 수 있는 갯수 * B가 선택할 수 있는 갯수


""" 내가 푼 풀이  
for i in range(n):
    for j in range(i+1,n):
        if datas[j] !=  datas[i]:
            result += 1 
"""

print(result)
