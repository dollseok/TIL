#SWEA 문제해결 기본 5186번 이진수2

'''
소수점 십진수 N을 이진수로 바꾸려한다.
'''


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    N = float(input())            # 소수점이 있는 숫자임으로 float 사용
    res = ''
    for i in range(1,13):         # 13자리 소수점까지만 봄으로 범위 설정
        if N == 0:                # N이 0이 되면 뒤에 볼 필요 없이 브레이크
            break
        if N >= 2**(-1 * i):      # 이진수 변환, N이 더 크면
            N -= 2**(-1 * i)      # 이진수 자리의 숫자만큼 빼주고
            res += '1'            # 결과에 1 추가
        else:
            res += '0'

    if N != 0:                    # 13자리 다했는데 0이 안되었으면
        res = 'overflow'          # overflow

    print(f'#{test_case}', res)






