'''
1719번 택배
오기직전 경로에 무엇이 있었는지 출력
'''
import heapq

def dijkstra(start, end):
    hq = []
    heapq.heappush(hq, (0,start))

    while hq:
        dist, node = heapq.heappop(hq)
        for next_dist, next_node in connect[node]:
            if dist_arr[start][next_node] < dist + next_dist:
                continue
            else:
                dist_arr[start][next_node] = dist + next_dist
                heapq.heappush(hq,(dist + next_dist, next_node))
                result[next_node][start] = node



v,e = map(int,input().split())
INF = int(1e9)

connect = [[] for _ in range(v+1)]
dist_arr = [[INF]*(v+1) for _ in range(v+1)] # 현재 연결되어 있는 거리
result = [[0]*(v+1) for _ in range(v+1)] # 어디로 가는 것이 가장 빠른 경로인지

for i in range(v+1):
    dist_arr[i][i] = 0
    result[i][i] = '-'

for _ in range(e):
    s,e,d = map(int,input().split())
    connect[s].append([d,e])
    connect[e].append([d,s])
    dist_arr[s][e] = d
    dist_arr[e][s] = d
    result[s][e] = e
    result[e][s] = s

# 출발지에서 그 지점으로 가는데 가장 빠른 경로 찾기
for i in range(1,v+1):
    dijkstra(i,v)

for i in range(1,v+1):
    print(*result[i][1:])
