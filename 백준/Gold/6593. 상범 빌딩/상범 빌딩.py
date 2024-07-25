'''
상범 빌딩

정육면체로 이루어진 빌딩
이동 동 서 남 북 상 하
1분들여 이동 가능
지나갈 수 있는 칸 = .
막혀있는 칸 = #

풀이
3차원 배열

'''

from collections import deque


def bfs(start_point):
    q = deque()
    q.append(start_point)

    while q:
        cl, cr, cc = q.popleft()
        # print(cl,cr,cc, '거리', distance[cl][cr][cc])

        for dl, dr, dc in directions:
            tl, tr, tc = cl + dl, cr + dr, cc + dc
            if 0 <= tl < L and 0 <= tr < R and 0 <= tc < C:
                if building[tl][tr][tc] == 'E':
                    return f'Escaped in {distance[cl][cr][cc] + 1} minute(s).'
                if building[tl][tr][tc] == '.' and distance[tl][tr][tc] == 0:
                    distance[tl][tr][tc] = distance[cl][cr][cc] + 1
                    q.append((tl, tr, tc))

    return 'Trapped!'

while True:

    # 입력
    L,R,C = map(int,input().split())
    if (L,R,C) == (0,0,0):
        break

    distance = [[[0]*C for _ in range(R)] for _ in range(L)]

    building = []

    for _ in range(L):
        building_floor = []
        for _ in range(R):
            building_floor.append(list(input()))
        blank = input()
        building.append(building_floor)


    # 시작점 찾기
    start = (0,0,0)
    end = (0,0,0)

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    start = (i,j,k)
                if building[i][j][k] == 'E':
                    end = (i,j,k)

    directions = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

    print(bfs(start))






