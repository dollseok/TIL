'''
14940번 쉬운 최단거리
'''

import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

arr = []
visited = [[False]*m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int,input().split())))



queue = deque()

# 시작 지점(목표 지점 체크)
for i in range(n):
    if queue:
        break
    for j in range(m):
        if arr[i][j] == 2:
            arr[i][j] = 0
            visited[i][j] = True
            queue.append([i,j])
            break

dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 끝까지 확인
while queue:
    x,y = queue.popleft()
    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < n and 0 <= cy < m and arr[cx][cy] == 1 and not visited[cx][cy]: # 범위 안에있고 옆에 있는게 1이면
            arr[cx][cy] = arr[x][y] + 1
            visited[cx][cy] = True
            queue.append([cx,cy])

# 방문할 수 없는 곳 -1로 만들기
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            arr[i][j] = -1

for i in range(n):
    print(*arr[i])

