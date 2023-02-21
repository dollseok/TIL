#SWEA 문제해결 기본 5105번 미로의 거리

import sys
sys.stdin = open("input.txt", "r")

# 수업 풀이



delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y, cnt):           # cnt : 몇칸 지나왔는지
    q = [(x, y, cnt)]
    while q:
        x, y, cnt = q.pop(0)
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] == 0:
                    maze[x][y] = 1
                    q.append((nx, ny, cnt+1))

                elif maze[nx][ny] == 3:
                    return cnt

    return 0


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    res = 0

    for x in range(n):
        for y in range(n):
            if maze[x][y] == 2:
                res = bfs(x, y, 0)    # 시작 위치 x,y

    print(f'#{tc}', res)


# 내가 푼 풀이

di = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(arr):
    global res
    visited = [[0]*(N+2) for _ in range(N+2)]
    q = [(si, sj)]
    visited[si][sj] = 1

    while q:
        ti, tj = q.pop(0)
        if arr[ti][tj] == 3:
            res = visited[ti][tj] - 2    # 거치는 칸의 개수이므로 시작,끝점을 빼준다
            break
        for k in range(4):
            if arr[ti + di[k][0]][tj + di[k][1]] == 0 or arr[ti + di[k][0]][tj + di[k][1]] == 3:
                if visited[ti + di[k][0]][tj + di[k][1]] == 0:
                    q.append((ti + di[k][0], tj + di[k][1]))
                    visited[ti + di[k][0]][tj + di[k][1]] = visited[ti][tj] + 1



T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    arr = [[1]*(N+2)] + arr + [[1]*(N+2)]
    res = 0

    # 시작점 찾기
    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] == 2:
                si, sj = i, j
                break

    # 탐색 with Queue
    bfs(arr)
    print(f'#{test_case}', res)
