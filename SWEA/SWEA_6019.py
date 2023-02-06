# SWEA 6019번 기차 사이의 파리

'''
간단하게 풀 수있다.
기차가 이동하는 시간 만큼 파리가 이동하는 것이다
기차의 총 이동시간과 파리의 속도만 기억해라
'''



# 1    # 테스트케이스 개수
# 250 10 15 20    #  첫 번째 테스트 케이스,
# D=250, A=10, B=15, F=20

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    i = 0
    Fly_h = D/(F+B)
    while True:
        if i % 2 != 0:
            Fly_h += (D - (Fly_h * (A+B)))/(F+A)
            i += 1
        elif i % 2 == 0:
            Fly_h += (D - (Fly_h * (A+B)))/(F+B)
            i += 1

        if Fly_h >= D/(A+B):
            break

    print(f'#{tc} {Fly_h * F}')
