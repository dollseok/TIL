# SWEA 1974번 스도쿠 검증

import sys
sys.stdin = open("input.txt", "r")


def sudoku_check(arr):    #0 혹은 1을 받아야함으로 함수를 정의

    for i in range(9):    # 가로의 합이 45인 것을 확인
        sum_width = 0
        for j in range(9):
            sum_width += arr[i][j]
        if sum_width != 45:
            return 0

    for j in range(9):    # 세로의 합이 45인 것을 확인
        sum_length = 0
        for i in range(9):
            sum_length += arr[i][j]
        if sum_length != 45 :
            return 0

    for i in range(3):    # 기준점을 기준으로 합이 45인 것을 확인
        for j in range(3):
            sum_sq = 0
            for k in range(3):
                for l in range(3):
                    sum_sq += arr[3*i+k][3*j+l]    # 기준점을 시작 0, 3, 6으로 함
            if sum_sq != 45:
                return 0

    return 1


T = int(input())
for test_case in range(1,T+1):
    sudoku = [list(map(int,input().split())) for _ in range(9)]

    print(f'#{test_case} {sudoku_check(sudoku)}')



