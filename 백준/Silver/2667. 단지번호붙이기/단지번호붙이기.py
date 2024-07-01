'''
2667번 단지 번호 붙이기

bfs로 연결되어있는 부분 모두 체크하기
단지의 개수와 각 단지 내 집 수 몇개 있는지 오름차순 정렬
'''

from collections import deque

n = int(input())

arr = [list(map(int,input())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]
sx,sy = 0,0

village = 0
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            # 여기 부터 bfs 시작
            cnt = 1
            q = deque()
            q.append([i,j])
            visited[i][j] = True
            while q:
                sx,sy = q.popleft()
                for k in range(4):
                    tx,ty = sx + dx[k], sy + dy[k]
                    if 0<=tx<n and 0<=ty<n:
                        if arr[tx][ty] == 1 and not visited[tx][ty]:
                            visited[tx][ty] = True
                            q.append([tx,ty])
                            cnt += 1
            village += 1
            result.append(cnt)

result.sort()
print(village)
for t in result:
    print(t)