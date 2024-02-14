from collections import deque

n,m = map(int,input().split())
maze = []
visited = [[0] * m for _ in range(n)]

for _ in range(n):
    maze.append(list(input()))

n = n-1
m = m-1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited[0][0] = True

queue = deque()
queue.append((0,0,0))

while queue:
    x,y,cnt = queue.popleft()
    if x == n and y == m:
        print(cnt+1)
        break
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <=tx<=n and 0<=ty<=m and maze[tx][ty] == '1' and not visited[tx][ty]:
            visited[tx][ty] = True
            queue.append((tx,ty,cnt+1))
