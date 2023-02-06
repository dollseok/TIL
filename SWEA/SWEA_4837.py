# SWEA 4837번 부분집합의 합

import sys
sys.stdin = open("input.txt", "r")

A = list(range(1, 13))

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())    # N 원소의 개수, K 부분집합의 총 합

    cnt = 0

    for i in range(1 << len(A)):   # 00000 00000 00 - 11111 11111 11  부분집합
        sum_list = []
        tot = 0
        for j in range(len(A)):
            if i & (1 << j):      # 1 10 100 1000 10000 10000 100000 .. 10000000000  & 연산자로 1이 겹치면 추가
                sum_list.append(A[j])     # 부분집합에 포함이 되면 하나씩 추가
                tot += A[j]               # 각 부분집합에 대한 총합을 미리 구해둠

        if len(sum_list) == N and tot == K:
            cnt += 1     # 조건에 맞는 것이 있으면 1씩 세어줌

    print(f'#{test_case} {cnt}')
