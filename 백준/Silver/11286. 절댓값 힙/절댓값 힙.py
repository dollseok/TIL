'''
11286번 절댓값 힙

heapq -> 절대값과 원본값을 함꼐 넣는다
'''

import heapq
import sys
input = sys.stdin.readline

n = int(input())

hq = []


for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(hq,(abs(x),x))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)