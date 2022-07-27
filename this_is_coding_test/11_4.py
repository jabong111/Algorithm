from collections import deque
import heapq
import sys
from tkinter import W

INF = int(1e9)
input = sys.stdin.readline


#갯수
n = int(input())
datas = list(map(int, input().split()))

datas.sort()
target = 1

for data in datas:
    if target < data: 
        break
    target += data

print(target)




