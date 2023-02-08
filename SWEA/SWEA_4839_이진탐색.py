# SWEA 4839번 이진탐색

import sys
sys.stdin = open("input.txt", "r")


def find_page(N, key):
    start = 1        # 책은 1페이지부터 시작이다
    end = N
    cnt = 0
    while start <= end:
        if key == end or key == start:    # 찾는 페이지가 첫페이지나 끝페이지라면
            return 0

        pivot = (start + end) // 2        # 중간 페이지
        if pivot == key:
            return cnt
        elif pivot > key:
            end = pivot
            cnt += 1
        else:
            start = pivot
            cnt += 1


T = int(input())
for test_case in range(1, T+1):
    P, A, B = map(int, input().split())

    if (find_page(P, A)) == (find_page(P, B)):
        winner = 0
    elif find_page(P, A) > find_page(P, B):
        winner = 'B'
    else:
        winner = 'A'

    print(f'#{test_case} {winner}')
