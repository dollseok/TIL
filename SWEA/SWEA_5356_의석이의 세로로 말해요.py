# SWEA 5356번 의석이의 세로로 말해요

'''
빈칸이 있으면 out of range
그 부분을 예외처리로 해주면 좋을 것 같음
'''

import sys
sys.stdin = open("input.txt", "r")

# 길이를 확인하는 함수
def my_len(a):
    cnt = 0
    for _ in list(a):
        cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T+1):
        arr = list(input() for i in range(5))
        read_string = ''

        # 가장 긴 라인 구하는 것
        max_line = 0
        for i in range(5):
            if max_line < my_len(arr[i]):
                max_line = my_len(arr[i])

        # index가 넘어가도 이어서 읽기
        for j in range(max_line):
            for i in range(5):
                try:
                    read_string += arr[i][j]
                except IndexError:
                    continue

        print(f'#{test_case}', read_string)

