'''
10026번 적록색약

적록색약 아닌 사람
R, G, B 세가지

적록색약인 사람
R-G 가 하나 처럼 보임 , B 두가지

bfs으로 풀면 될 것 같음
n : 최대 100
10000 개
'''
from collections import deque

n = int(input())
arr = []
visited_rgb = [[False] * n for _ in range(n)]
visited_rb = [[False] * n for _ in range(n)]


for _ in range(n):
    arr.append(list(input()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

result_rgb = 0
result_rb = 0


def bfs_rgb(i,j,color):
    global result_rgb
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            cx, cy = x + dx[k], y + dy[k]
            if 0 <= cx < n and 0 <= cy < n and not visited_rgb[cx][cy]:
                if arr[cx][cy] == color:
                    q.append((cx,cy))
                    visited_rgb[cx][cy] = True

    result_rgb += 1


def bfs_rb(i, j, color):
    global result_rb
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            cx, cy = x + dx[k], y + dy[k]
            if 0 <= cx < n and 0 <= cy < n and not visited_rb[cx][cy]:
                if color == "R" or color == "G":
                    if arr[cx][cy] == "R" or arr[cx][cy] == "G":
                        q.append((cx, cy))
                        visited_rb[cx][cy] = True
                else:
                    if arr[cx][cy] == color:
                        q.append((cx, cy))
                        visited_rb[cx][cy] = True

    result_rb += 1


for i in range(n):
    for j in range(n):
        if not visited_rb[i][j]:
            bfs_rb(i,j,arr[i][j])
        if not visited_rgb[i][j]:
            bfs_rgb(i, j, arr[i][j])

print(result_rgb,result_rb)





