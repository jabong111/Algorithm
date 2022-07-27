from collections import deque
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

N = int(input())
s = input()

length = len(s)-1

last = s[length-1]

list_map = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v']

if last in list_map:
    print(1)
else:
    print(0) 


