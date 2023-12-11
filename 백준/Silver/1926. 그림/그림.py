"""
1. 아이디어
- 2중 for 문 -> 값 1 && 방문 x => BFS
- BFS 돌면서 그림개수 +1 , 최대값 갱신

2. 시간 복잡도
- BFS = O(V+E)
- V = m * n
- E = V * 4
O(V+4V) = O(5V) => m 최대 500 , n 최대 500

- V+E = 5 * 250000 = 100만 <2억 가능

3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(y,x):
    res = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == 1 and visited[ny][nx] == False:
                    res += 1
                    visited[ny][nx] = True
                    q.append((ny,nx))
    return res

cnt = 0
maxV = 0
for j in range(n):
    for i in range(m):
        if arr[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            # 전체 그림 개수 +1
            cnt += 1
            # BFS > 그림 크기 구하기
            # 최대값 갱신
            maxV = max(maxV, bfs(j,i))


print(cnt)
print(maxV)