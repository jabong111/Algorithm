from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

T = int(input())

answer = []
for i in range(T):
    sum = 0
    N = int(input())
    datas = list(map(int,input().split()))
    for j in datas:
        sum += j
    answer.append(sum)


for sum in answer:
    print(sum)
