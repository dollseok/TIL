# SWEA 1979번 어디에 단어가 들어갈 수 있을까?

'''
NxN 크기의 단어 퍼즐
특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 개수를 출력

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())    # N = 가로 세로 길이, K = 단어의 길이
    cnt = 0
    arr = list(input() for _ in range(N))
    new_arr = list((arr[i].replace(' ', '')) for i in range(N))   # 문자열로 받은 arr의 공백을 지워줌

    print(arr)         # ['0 0 1 1 1', '1 1 1 1 0', '0 0 1 0 0', '0 1 1 1 1', '1 1 1 0 1']
    print(new_arr)     # ['00111', '11110', '00100', '01111', '11101']

    for i in range(N):
        check_list = new_arr[i].split('0')

        # print(check_list)
        '''
        split을 통해서 그 안에 덩어리들이 문자들어가는 개수와 맞는 지 확인 
        ['', '', '111']
        ['1111', '']
        ['', '', '1', '', '']
        ['', '1111']
        ['111', '1']
        '''
        for i in check_list:
            if '1'*K == i:     # K=3이라는 것은 111이 있는지 확인하면 되는 것
                cnt += 1

    for j in range(N):
        new_line = ''       # 세로줄을 만들어줄 새로운 라인을 변수를 만들어 줌
        for i in range(N):
            new_line += new_arr[i][j]    # 문자열이니 더하면 이어진다
        check_list = new_line.split('0')
        for i in check_list:
            if '1'*K == i:
                cnt += 1

    print(f'#{test_case} {cnt}')
