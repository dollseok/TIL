# SWEA 1954번 달팽이 숫자


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    di = [0, 1, -1, 0]
    dj = [1, 0, 0, -1]
    tot_cnt = 0
    num = 0
    ci, cj = 0, 0
    k = 0

    while tot_cnt != N**2:
        if 0 <= ci < N and 0 <= cj < N and arr[ci][cj] == 0:
            num += 1
            arr[ci][cj] = num
            tot_cnt += 1

        else:
            ci -= di[k]
            cj -= dj[k]
            k = (k+1) % 4

        ci += di[k]
        cj += dj[k]

    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])