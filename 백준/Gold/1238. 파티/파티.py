'''
1238번 파티

단방향 도로
x번 마을에 가야함
x번까지 가는데 가장 오랜 시간이 걸리는 사람의 소요시간

시작점을 x번 마을

1. 2번에서 시작하는 방식
- 역순으로 올라가서 가장 멀리까지 있는 것을 구하는 방식
- bfs

2. 모든 지점에서 2번으로 가는 방식
- 시간 초과 가능성 다분

3. 최단 거리 다익스트라 알고리즘
- 이거는 외워야하나..?
'''

import heapq


def dijkstra(start,end):
    q = []
    node = [INF]*(n+1)
    heapq.heappush(q,(0,start))
    node[start] = 0

    while q:
        distance, now = heapq.heappop(q)
        if node[now] < distance: continue

        for i in arr[now]:
            dst = i[0]
            cost = distance + i[1]

            if cost < node[dst]:
                heapq.heappush(q,(cost,dst))
                node[dst] = cost

    return node[end]

n,m,x = map(int,input().split())
arr = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(m):
    i,j,w = map(int,input().split())
    arr[i].append((j,w))

result = 0
for i in range(1,n+1):
    if i == x: continue
    result = max(result,dijkstra(i,x)+dijkstra(x,i))

print(result)