#SWEA 2001번 파리 퇴치

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N : 영역의 넓이 , M : 파리채 사이즈

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt_flys = 0

    for i in range(N-M+1):
        for j in range(N-M+1):     # 기준점이 N-M 인덱스까지임
            cnt_flys = 0
            for k in range(M):     # 기준점으로부터 파리채의 범위
                for a in range(M):
                    cnt_flys += arr[i+k][j+a]

            if max_cnt_flys < cnt_flys:
                max_cnt_flys = cnt_flys

    print(f'#{test_case} {max_cnt_flys}')

