#SWEA 1989번 초심자의 회문 검사

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = input()
    res = 0
    if N == N[::-1]:
        res = 1

    print(f'{test_case} {res}')