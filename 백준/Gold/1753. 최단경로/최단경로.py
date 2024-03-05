'''
1753번 최단 경로

다익스트라 전형적인 문제
'''

import heapq
import sys

input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0,start))

    while hq:
        dist,node = heapq.heappop(hq)

        for next in arr[node]:
            if dist_arr[next[1]] < dist + next[0]: # 이미 자리 잡은 거리가 더 작으면 갱신x
                continue
            else:
                dist_arr[next[1]] = dist + next[0]
                heapq.heappush(hq,(dist_arr[next[1]], next[1]))



v,e = map(int,input().split())
start_point = int(input())
INF = int(1e9)

arr = [[] for _ in range(v+1)]
dist_arr = [INF]*(v+1)
dist_arr[start_point] = 0

for _ in range(e):
    s,e,d = map(int,input().split())
    arr[s].append([d, e])

dijkstra(start_point)

for i in range(1,v+1):
    if dist_arr[i] == INF:
        print('INF')
    else:
        print(dist_arr[i])
