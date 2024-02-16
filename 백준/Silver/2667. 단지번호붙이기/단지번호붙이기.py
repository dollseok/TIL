from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

result = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and not visited[i][j]:
            queue = deque()
            queue.append((i,j))
            cnt = 0
            while queue:
                x,y= queue.popleft()
                cnt += 1
                visited[x][y] = True
                for k in range(4):
                    tx = x + dx[k]
                    ty = y + dy[k]
                    if 0 <= tx < n and 0 <= ty < n:
                        if arr[tx][ty] == '1' and not visited[tx][ty]:
                            visited[tx][ty] = True
                            queue.append((tx,ty))


            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)