from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline


data = input()


data_len = len(data)-1
datas = []

for i in range(data_len):
    datas.append(data[i])


first = 0
last = 0

#처음 
for i in range(data_len//2):
    first += int(datas[i])

#끝
for i in range(data_len//2, data_len):
    last += int(datas[i])

if first == last:
    print("LUCKY")
else:
    print("READY")


