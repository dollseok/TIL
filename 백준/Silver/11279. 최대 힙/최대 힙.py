'''
11279번 최대힙

heapq 자체는 최소힙
-> 최대힙은 - 붙여서 저장하고 뺄때 -1 곱합

'''

import heapq
import sys

input = sys.stdin.readline
n = int(input())
hq = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if hq:
            print(heapq.heappop(hq) * -1)
        else:
            print(0)
    else:
        heapq.heappush(hq,-x)