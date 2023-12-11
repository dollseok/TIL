"""
1. 아이디어
- 2중 for 문 -> 값 1 && 방문 x => BFS
- BFS 돌면서 한 부분의 개수 +1, 최소 배추 흰지렁이 마리 수

2. 시간 복잡도
- BFS = O(V+E)
- V = m * n
- E = V * 4
O(V+4V) = O(5V) => m 최대 50 , n 최대 50

- V+E = 5 * 2500 = 1만 <2억 가능

3. 자료구조
- 밭의 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M,N,K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        i,j = map(int, input().split())
        arr[j][i] = 1

    dx = (0,1,0,-1)
    dy = (1,0,-1,0)
    def bfs(y,x):
        q = [(y,x)]
        while q:
            ey,ex = q.pop()
            for k in range(4):
                ny = ey + dy[k]
                nx = ex + dx[k]
                if 0 <= ny < N and 0 <= nx < M:
                    if arr[ny][nx] == 1 and visited[ny][nx] == False:
                        visited[ny][nx] = True
                        q.append((ny,nx))

    for j in range(N):
        for i in range(M):
            if arr[j][i] == 1 and visited[j][i] == False:
                cnt += 1
                bfs(j,i)

    print(cnt)