from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

s = input()

count_zero = 0 # 연속된 0 횟수 
count_one = 0  # 연속된 1 횟수 

if  s[0] == '0':    
    count_zero += 1 
else:
    count_one += 1

for i in range(len(s)-2):
    if s[i] != s[i+1]: #다음 값이 다르면
        if s[i+1] == '1':
            count_one += 1
        else:
            count_zero += 1
        
if int(s) == 0 or s == '1' * (len(s) - 1):
    result = 0
else:
    result = min(count_one, count_zero)

print(result)


"""
count_zero = 0 #모두 0으로 만드는 횟수
count_one = 0  #모두 1로 만드는 횟수

if  s[0] == '0':    
    count_one += 1 
else:
    count_zero += 1

for i in range(len(s)-2):
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            count_one += 1
        else:
            count_zero += 1

result = min(count_zero, count_one)

print(result)
"""

