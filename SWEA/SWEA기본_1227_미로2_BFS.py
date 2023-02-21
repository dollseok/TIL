#SWEA 문제해결 기본 1227번 미로2

import sys
sys.stdin = open("input.txt", "r")

delta = [(1,0), (0,1), (-1, 0), (0, -1)]

def bfs(x, y):
    q = [(x, y)]

    while q:
        x, y = q.pop(0)
        for dx,dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 16 and 0 <= ny < 16:
                if arr[nx][ny] == 0:
                    arr[x][y] = 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 3:
                    return 1

    return 0


for _ in range(10):
    test_case = int(input())

    arr = [list(map(int,input())) for _ in range(16)]

    print(f'#{test_case}', bfs(1,1))
