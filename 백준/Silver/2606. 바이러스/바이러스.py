from collections import deque

n = int(input())
m = int(input())
arr = [[0] * n for _ in range(n)]
visited = [False] * n

for _ in range(m):
    s,e = map(int,input().split())
    arr[s-1][e-1] = 1
    arr[e-1][s-1] = 1

# for i in range(n):
    # print(arr[i])

queue = deque([0])
visited[0] = True
cnt = 0

while queue:
    start = queue.popleft()
    for i in range(n):
        if arr[start][i] == 1 and visited[i] == False:
            queue.append(i)
            visited[i] = True
            cnt += 1

print(cnt)
