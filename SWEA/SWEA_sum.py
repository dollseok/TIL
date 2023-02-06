#SWEA 문제해결 기본 Sum

import sys
sys.stdin = open("input.txt", "r")


for _ in range(1, 11):
    test_case = int(input())

    arr = list(list(map(int, input().split())) for _ in range(100))
    # print(arr)

    sum_max = 0

    for i in range(100):
        sum_width = 0    # 가로 방향으로의 합
        # sum(arr[i])
        for j in range(100):
            sum_width += arr[i][j]
        # print(sum_width)
        if sum_max < sum_width:    # 가로 방향의 합이 최대인가?
            sum_max = sum_width

    for j in range(100):   # 세로 방향으로의 합
        sum_length = 0
        for i in range(100):
            sum_length += arr[i][j]

        if sum_max < sum_length:   # 세로 방향의 합이 최대인가?
            sum_max = sum_length

    for i in range(100):
        for j in range(100):
            sum_cross = 0     # 정상 대각선 방향의 합
            if i == j:
                sum_cross += arr[i][j]

        if sum_max < sum_cross:
            sum_max = sum_cross

    for i in range(100):
        for j in range(100):
            sum_cross_rev = 0   # 반대 대각선 방향의 합
            if i + j == (100 - 1):    # 반대 대각선은 인덱스 합이 99이다
                sum_cross_rev += arr[i][j]
        if sum_max < sum_cross_rev:
            sum_max = sum_cross_rev

    print(f'#{test_case} {sum_max}')