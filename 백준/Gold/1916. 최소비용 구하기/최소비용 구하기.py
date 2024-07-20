'''
최소비용 구하기
n개의 도시, m개의 버스
a->b 가는데 버스 비용 최소화

입력
n
m
출발지 도착지 버스비용
...
a,b

내 풀이

1.
전형적인 백트래킹? -> x 더 싼 경로가 이후에 나올수도 있기 때문

2.
dfs -> 5가 나올 떄까지 탐색
=> 시간 초과

3.
다익스트라


'''

import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
cost_arr = [INF] *(n+1)

for _ in range(m):
    s,e,c = map(int,input().split())
    graph[s].append((e,c))

start_point,end_point = map(int,input().split()) # start point, end point

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 비용, 시작점

    while q:
        cost,now = heapq.heappop(q)

        if cost_arr[now] < cost: # 뽑은 거리가 지금 저장되어있는 거리보다 크면 패스
            continue

        for i in graph[now]: # end , cost
            new_cost = cost + i[1]
            if new_cost < cost_arr[i[0]]:
                cost_arr[i[0]] = new_cost
                heapq.heappush(q,(new_cost,i[0]))

cost_arr[start_point] = 0
dijkstra(start_point)

print(cost_arr[end_point])