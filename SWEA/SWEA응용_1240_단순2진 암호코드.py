#SWEA 문제해결 응용 1240번 단순 2진 암호코드

'''
암호코드 삽입하여 송출
1. 8개의 숫자로 이루어져있다
2. 홀수자리의 합 x 3 + 짝수자리의 합이 10 배수

암호 코드 인식하는 스캐너 개발
뒤에서부터 스캔 1만나면 그자리부터 56개
'''

import sys
sys.stdin = open("input.txt", "r")

def pick(data,m):                          # m : 가로
    for line in data:
        if line == '0' * m:                # 0만 가득차있는 함수는 버린다
            continue
        else:
            for j in range(m-1, 0, -1):    # 뒤에서부터 확인 (시작점이 0인경우는 있지만 마지막이 1이 아닌 경우는 없음)
                if line[j] == '1':                   # 1을 찾으면
                    data_endpoint = j                # j가 끝점
                    data_startpoint = j - 56 + 1     # 시작점은 j로부터 56번째 앞에

                    return line[data_startpoint : data_endpoint + 1]    # 데이터를 리턴

data_dict = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
             '0110001':5,'0101111':6, '0111011':7, '0110111':8, '0001011':9}

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    data = [input() for _ in range(N)]

    # [1] 데이터 추출
    main_data = pick(data, M)      # 데이터 중에 필요있는 한줄만 픽해오는 함수
    # print(main_data)             # 01110110110001011101101100010110001000110100100110111011

    # [2] 데이터 변환
    t_list = []                    # transform list
    for i in range(8):
        a = main_data[7 * i : 7 * (i+1)]    # 슬라이싱으로 파트 별로 잘라줌
        t_list.append(data_dict[a])
    # print(t_list)            # [7, 5, 7, 5, 5, 0, 2, 7]

    # [3] 홀수번째 합, 짝수번째 합 구함
    odd_sum = 0
    even_sum = 0
    for i in range(4):     # 8자리 암호
        odd_sum += t_list[2*i]
        even_sum += t_list[2*i+1]

    # [4] 옳은 암호인지 확인
    if (odd_sum*3 + even_sum) % 10 == 0:
        res = odd_sum + even_sum
    else:
        res = 0

    print(f'#{test_case}', res)
