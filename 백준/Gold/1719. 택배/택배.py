'''
1719번 택배
'''

from heapq import heappop,heappush

def dijkstra(start,n):
    global dist_arr,res

    hq = []
    for i in range(1,n+1):
        if i == start:
            continue
        heappush(hq, (dist_arr[start][i], i))

    while hq:
        dist, node = heappop(hq)
        if dist_arr[start][node] < dist: # 거리가 길면 넘어감
            continue
        for neighbor in range(1,n+1):
            if node == neighbor or start == neighbor:
                continue
            if dist + dist_arr[node][neighbor] < dist_arr[start][neighbor]:
                dist_arr[start][neighbor] = dist + dist_arr[node][neighbor]
                heappush(hq,(dist+dist_arr[node][neighbor],neighbor))

                res[start][neighbor] = res[start][node]


n,m = map(int,input().split())
INF = 1e9
dist_arr = [[INF]*(n+1) for _ in range(n+1)]
res = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    res[i][i] = '-'

for _ in range(m):
    a,b,dst = map(int,input().split())
    dist_arr[a][b] = dst
    dist_arr[b][a] = dst
    res[a][b] = b
    res[b][a] = a

for i in range(1,n+1):
    dijkstra(i,n)

for line in res[1:]:
    print(*line[1:])