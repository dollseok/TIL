#SWEA 문제해결 기본 4615번 재미있는 오셀로 게임

import sys
sys.stdin = open("input.txt", "r")

di = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

T = int(input())
for test_case in range(1, T+1):

    N,M = map(int, input().split())


    arr = [[0]*(N+2) for _ in range(N+2)]          #위아래 패딩 추가한 arr
    # 시작 좌표 설정
    arr[N//2][N//2] = 2                 # 백돌 2, 정방향 대각선 중앙
    arr[N // 2 + 1][N // 2 + 1] = 2
    arr[N // 2 + 1][N // 2] = 1         # 흑돌 1  역방향 대각선 중앙
    arr[N // 2][N // 2 + 1] = 1

    for _ in range(M):
        i, j, c = map(int, input().split())
        arr[i][j] = c                   # i,j의 위치에 c를 놓을 것임

        if c == 1:                      # 흑돌일 때
            for k in range(8):          # 8방향 확인

                ti = i + di[k][0]       # 이동한 방향에 확인
                tj = j + di[k][1]
                temp_list = []          # 임시 리스트
                if arr[ti][tj] == 2:    # 그 방향에 백돌이 있다면
                    # temp_list.append((ti, tj))
                    while True:
                        temp_list.append((ti, tj))   # 임시 리스트에 추가를 해주고
                        ti += di[k][0]               # 이동한 좌표를 임시 좌표에 넣어주고
                        tj += di[k][1]

                        if arr[ti][tj] == 1:         # 임시 좌표 자리에 백돌이 있다면
                            for c in temp_list:      # 임시 리스트에 있는 좌표들을 백돌로 바꾸어줌
                                ci, cj = c
                                arr[ci][cj] = 1
                            break                    # 그리고 브레이크 ( 다음턴 넘김 )

                        elif arr[ti][tj] == 0:       # 만약에 0,보드의 끝이나온다면 끝냄
                            break
                        elif arr[ti][tj] == 2:       # 2가 또 나온다면 while문 반복 (임시좌표를 리스트에 추가하고 진행)
                            continue
        # 흑돌일 때도 마찬가지로 진행
        if c == 2:
            for k in range(8):

                ti = i + di[k][0]
                tj = j + di[k][1]
                temp_list = []
                if arr[ti][tj] == 1:
                    # temp_list.append((ti, tj))
                    while True:
                        temp_list.append((ti, tj))
                        ti += di[k][0]
                        tj += di[k][1]

                        if arr[ti][tj] == 2:
                            for c in temp_list:
                                ci, cj = c
                                arr[ci][cj] = 2
                            break

                        elif arr[ti][tj] == 0:
                            break
                        elif arr[ti][tj] == 1:
                            continue

    # 정답에서 원하는 흑돌 백돌의 개수 확인
    black_cnt = 0
    white_cnt = 0
    res = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                black_cnt += 1
            elif arr[i][j] == 2:
                white_cnt += 1

    if black_cnt > white_cnt:
        res = black_cnt
    else:
        res = white_cnt

    print(f'#{test_case} {black_cnt} {white_cnt}')


