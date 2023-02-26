#SWEA 2805번 농작물 수확하기

'''
농장크기는 항상 홀수
수확은 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sum_ = 0
    center = (N - 1) // 2  # 센터지점

    for i in range(center + 1):    # 센터 기준 대칭으로 볼 것
        if i < center:
            sum_ += sum(arr[i][(center - i):(center + i + 1)])
            sum_ += sum(arr[N-1-i][(center - i):(center + i + 1)])
        elif i == center:          # 센터는 따로 더한다
            sum_ += sum(arr[i])

    print(f'#{test_case}', sum_)
