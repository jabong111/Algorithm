from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

s = input()

result = int(s[0])

for i in range(1, len(s)-1):
    data = int(s[i])
    if data <= 1 or result <= 1:
        result += data
    else:
        result *= data

print(result)
