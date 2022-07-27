from collections import deque
import heapq
import string
import sys

INF = int(1e9)
input = sys.stdin.readline

strings = input() 

sum  = 0;

alpha = []
result = "" 

for i in range(len(strings)-1):
    if strings[i] >= '0' and strings[i] <= '9':
        sum += int(strings[i])
    else:
        alpha.append(strings[i])

alpha.sort()

#문자 리스트를 문자열로 변환
for i in alpha:
    result += i
#숫자 합치기
result += str(sum)

print(result)