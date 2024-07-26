'''
불

동서남북 방향으로 인접한 빈 공간 이동 가능, 1초 걸림
벽 통과 x, 불이 옮겨진 칸 & 붙으려는 칸 이동 x,

*이 먼저, @이 다음

'''

from collections import deque


def bfs(fire,start):
    q = deque(fire + start)

    while q:
        cy, cx, state = q.popleft()
        for i in range(4):
            ty = cy + dy[i]
            tx = cx + dx[i]
            if ty >= h or ty < 0 or tx >= w or tx < 0:  # 도착 조건
                if (arr[cy][cx] == '.' or arr[cy][cx]=='@') and distance[cy][cx] != -1:
                    return distance[cy][cx] + 1
            else:
                if state == '*':
                    if arr[ty][tx] == '.' and distance[ty][tx] == 0:
                        distance[ty][tx] = -1
                        q.append((ty,tx,'*'))
                elif state == '@':
                    if arr[ty][tx] == '.' and distance[ty][tx] == 0:
                        distance[ty][tx] = distance[cy][cx] + 1
                        q.append((ty,tx,'@'))

    return 'IMPOSSIBLE'

t = int(input())

for _ in range(t):
    w,h = map(int,input().split())
    arr = [list(input()) for _ in range(h)]
    distance = [[0]*w for _ in range(h)]

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    fire_list = []
    start_list = []

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                distance[i][j] = -1
                fire_list.append((i,j,'*'))
            elif arr[i][j] == '@':
                start_list.append((i,j,'@'))

    print(bfs(fire_list,start_list))

'''
1
7 5
###.###
@....*#
#.....#
#.....#
.######

'''