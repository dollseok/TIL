# SWEA 1954번 달팽이 숫자

'''
시계방향으로 N*N의 표에 숫자를 넣는 문제
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]     # 모든 요소가 0인 N*N의 arr

    # 시계방향 Direction 우, 하, 좌, 상
    di = [0, 1, 0, -1]  # 순서 중요하지 않음
    dj = [1, 0, -1, 0]

    #변수 설정
    # tot_cnt = 0       # 모든 칸이 다 찼을 때 끝내기 위한 변수  # num 으로 대체 가능, 삭제
    num = 0           # 넣어주는 숫자
    ci, cj = 0, 0     # 시작 위치 & 현재 위치
    k = 0

    while num != N**2:
        if 0 <= ci < N and 0 <= cj < N and arr[ci][cj] == 0:    # 범위를 넘어가지 않고, 그 자리를 지나가지 않았을 때(0일 때)
            num += 1
            arr[ci][cj] = num
            # tot_cnt += 1

        else:               # 범위를 넘어갔거나, 그 자리를 이미 지나갔을 때
            ci -= di[k]     # 원래 자리로 돌아옴
            cj -= dj[k]
            k = (k+1) % 4   # 방향 전환(3 이하의 수로 direction이 돌아감)

        ci += di[k]         # 옮긴 방향으로 옮겨줌
        cj += dj[k]

    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])