#백준 1003번 피보나치 함수

'''
https://www.acmicpc.net/problem/1059

처음엔 재귀로 풀어서 시간 초과
두번째는 import sys를 빼먹어서 Nameerror
'''


def fibo(n):
    f = [0,1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

import sys
input = sys.stdin.readline
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt1 = fibo(N)               # 피보나치 N번째가 1이 호출된 횟수
    cnt0 = fibo(N-1)             # 피보나치 N-1번째가 0이 호출된 횟수
    print(cnt0, cnt1)

