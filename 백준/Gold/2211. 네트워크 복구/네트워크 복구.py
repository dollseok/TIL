'''

1번 컴퓨터가 슈퍼 컴퓨터
1과 모두 연결되어있어야함 근데 다른 컴퓨터랑 연결되는게 더빠를 수도 있음

최단 거리
양방향 통신
visited로 처리
다익스트라?

'''

import heapq


def dijkstra():
    hq = []
    heapq.heappush(hq,[0,1])
    velocity[1] = 0
    while hq:
        v,current = heapq.heappop(hq)

        if velocity[current] < v:
            continue

        for i in network[current]:
            if v + i[0] < velocity[i[1]]:
                connect[i[1]] = current
                velocity[i[1]] = v + i[0]
                heapq.heappush(hq,(v+i[0], i[1]))

N,M = map(int,input().split())
INF = 1e9
network = [[] for _ in range(N+1)]
velocity = [INF]*(N+1)
connect = [-1]*(N+1)

for _ in range(M):
    a,b,v = map(int,input().split())
    network[a].append([v,b])
    network[b].append([v,a])


dijkstra()
result = []
for i in range(1,N+1):
    if connect[i] != -1:
        result.append((connect[i],i))

print(len(result))
for r in result:
    print(r[0],r[1])