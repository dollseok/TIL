'''
16928번 뱀과 사다리 게임

주사위 1~6
10*10 게임판

bfs
'''

from collections import deque

visited = [False] * 101
arr = [0] * 101

n,m = map(int,input().split())

# 사다리 (올라감)
ladder = {}
for _ in range(n):
    s,e = map(int,input().split())
    ladder[s] = e
# 뱀 (내려감)
snake = {}
for _ in range(m):
    s, e = map(int, input().split())
    snake[s] = e

q = deque()
q.append(1)
flag = True

while q and flag:
    now = q.popleft()

    for move in range(1,7):
        current = now + move

        if 1 <= current <= 100 and not visited[current]:
            if current in ladder.keys():
                current= ladder[current]

            if current in snake.keys():
                current = snake[current]

            if not visited[current]:
                q.append(current)
                visited[current] = True
                arr[current] = arr[now] + 1

print(arr[100])
