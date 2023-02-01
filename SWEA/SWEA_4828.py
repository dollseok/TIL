# SWEA 4828번 min-max
'''
max, min없이 최대값 최소값의 차이를 구하는 알고리즘
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    max_L, min_L = L[0], L[0]
    for i in range(N):
        if L[i] > max_L:
            max_L = L[i]
        elif L[i] < min_L:
            min_L = L[i]

    print(f'#{test_case} {max_L - min_L}')