#SWEA 1859번 백만장자 프로젝트

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    sale_price = list(map(int, input().split()))
    max_price = sale_price[-1]
    total_plus = 0

    for i in range(N-2,-1,-1):
        if max_price < sale_price[i]:
            max_price = sale_price[i]
        else:
            total_plus += max_price - sale_price[i]

    print(f'#{test_case} {total_plus}')



