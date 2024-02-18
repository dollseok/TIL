'''
bfs로 카운트
'''

from collections import deque

m,n = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

start_point = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            start_point.append((i,j))

cnt = 0

while start_point:
    x,y = start_point.popleft()
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < m:
            if arr[tx][ty] == 0:
                arr[tx][ty] = arr[x][y] + 1
                cnt = max(arr[tx][ty], cnt)
                start_point.append((tx,ty))


for i in range(n):
    if 0 in arr[i]:
        cnt = -1
        break

if cnt == -1:
    print(cnt)
elif cnt == 0:
    print(cnt)
else:
    print(cnt - 1)
