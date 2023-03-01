# SWEA 4673번 러시아 국기같은 깃발

'''
N행 M열
가장 적게 새로 칠해서 만든 러시아 국기
칠한 개수의 최솟값을 구하는 문제

완전 탐색으로 하나하나 체크해서 프린트
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    data = [list(input()) for _ in range(N)]
    mn = 5000000

    for W in range(N-2):               # 뒤에 B,R이 한줄씩은있으니 N-2까지
        for B in range(W+1, N-1):      # W 이후 부터 뒤에 R이 한줄은 있으니 N-1까지 / W,B가 정해지면 R은 자동으로 정해짐
            cnt = 0                    # cnt 초기화
            for i in range(W+1):       # W 범위 안에서
                for k in data[i]:
                    if k != 'W':       # W 아닌 것을 센다
                        cnt += 1
            for i in range(W+1, B+1):  # B 범위 안에서
                for k in data[i]:
                    if k != 'B':       # B 아닌 것을 센다
                        cnt += 1
            for i in range(B+1, N):    # R 범위 안에서
                for k in data[i]:
                    if k != 'R':       # R 아닌 것을 센다
                        cnt += 1

            if mn > cnt:               # cnt가 최소라면 가장 적게 뒤집어서 만든 것
                mn = cnt


    print(f'#{test_case}', mn)







