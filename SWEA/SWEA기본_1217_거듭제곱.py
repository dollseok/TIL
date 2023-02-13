#SWEA 문제해결 기본 1217번 거듭제곱

import sys
sys.stdin = open("input.txt", "r")

# 연속 곱을 구하는 함수 정의
def multi(N,M):
    if M != 0:                     # M이 0일 때까지
        return multi(N,M-1) * N    # 함수를 재호출
    return 1                       # 마지막에는 1을 꺼내줌

for _ in range(10):
    test_case = int(input())
    N, M = map(int, input().split())
    print(f'#{test_case}', multi(N, M))
