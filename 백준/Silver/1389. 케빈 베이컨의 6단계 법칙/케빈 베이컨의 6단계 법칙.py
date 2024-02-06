from collections import deque

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        target = queue.popleft()
        for i in arr[target]:
            if visited[i] == 0:
                visited[i] = visited[target] + 1
                queue.append(i)

for _ in range(m):
    #양방향 친구
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

res = []

for i in range(1,n+1):
    visited = [0]*(n+1)
    bfs(i)
    res.append(sum(visited))

print(res.index(min(res)) + 1)

