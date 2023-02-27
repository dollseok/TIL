#SWEA 문제해결 기본 5185번 이진수

'''
16진수
1~9, A : 10 B: 11 C: 12 D: 13 E: 14 F: 15
16진수 한자리는 2진수의 4자리
'''


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    N, hexa = input().split()
    bin_res = ''

    for i in range(int(N)):
        res = ''
        for j in range(4):
            if int(hexa[i], 16) & (1<<j):     # 앞에부터 확인해서 뒤집어져서 나온다.
                res += '1'
            else:
                res += '0'

        res = res[::-1]                       # 각 숫자별로 이진수로 변환한 4글자를 뒤집어서 최종에 넣음
        bin_res += res


    print(f'#{test_case}', bin_res)