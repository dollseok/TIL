#SWEA 문제 해결 기본 1226번 미로 1

import sys
sys.stdin = open("input.txt", "r")

delta = [(1,0), (0,1), (-1, 0), (0, -1)]

def bfs(x, y):
    q = [(x, y)]        # 시작점 좌표를 튜플로 넣어줌

    while q:
        x, y = q.pop(0)
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0:     # 이동한 곳이 통로라면
                    arr[x][y] = 1        # 방문했던 이전 장소를 1로 막아버림
                    q.append((nx, ny))   # 새로운 좌표를 queue에 넣음
                elif arr[nx][ny] == 3:   # 3이라면 도착한 것임으로 1을 반환
                    return 1

    return 0   # while문 다 돌았는데 3을 못만났으므로 0을 반환


for _ in range(10):
    test_case = int(input())
    N = 100
    arr = [list(map(int, input())) for _ in range(N)]

    print(f'#{test_case}', bfs(1, 1))       # 시작점은 무조건 1, 1