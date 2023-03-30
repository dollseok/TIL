# SWEA 5209번 최소 생산 비용

'''
각 제품에 대한 각 공장별 생산 비용,
전체 제품을 생산하는데 최소 생산 비용을 계산하는 프로그램을 만들어라
'''

import sys
sys.stdin = open('input.txt', 'r')

def backtracking(arr, row):
    global N, sum_, min_sum
    if row == N:                    # 가장 아래줄까지 도착했을 때
        if min_sum > sum_:
            min_sum = sum_
        return
    else:
        if sum_ > min_sum:          # 가장 아래줄까지 도달 전인데 합계의 값이 최소값보다 커졌을 때
            return

    for i in range(N):
        if visited[i] == 0:         # 하나의 공장당 하나의 제품임으로 visited사용

            sum_ += arr[row][i]     # 합계를 더해주고
            visited[i] = 1          # 공장을 돌리는 중이라는 표시
            row += 1                # 다음 제품 확인

            backtracking(arr,row)

            row -= 1
            visited[i] = 0
            sum_ -= arr[row][i]




T = int(input())
for test_case in range(1, T+1):
    N = int(input())            # 제품의 개수
    arr = [list(map(int,input().split())) for _ in range(N)]
    sum_ = 0
    min_sum = 9999999
    visited = [0]*N
    backtracking(arr,0)

    print(f'#{test_case}', min_sum)
