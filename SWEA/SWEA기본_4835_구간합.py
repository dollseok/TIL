# SWEA [파이썬 SW 문제해결 기본] 4835번 구간합
'''
전체에서 처음부터 끝까지 각 구간을 나누어 그만큼의 합을 구하는 것
'''

import sys
sys.stdin = open("input.txt", "r")

# 나의 풀이
# T = int(input())
# for test_case in range(1, T+1):
#
#     N, M = list(map(int, input().split()))    # N,M을 받음
#     L = list(map(int, input().split()))       # list를 받음
#
#     part_sum_lst = [0] * (N - M + 1)    # 사이즈가 N-M+1인 리스트를 만듦
#
#     for i in range(N-M+1):    # M개씩 합을 받으면  N-M+1개의 합들이 만들어질 것
#
#         for j in range(M):
#             part_sum_lst[i] += L[i+j]   # i에서 i+M-1까지 (M개) 의 합을 각 원소에 받음
#
#     min_part, max_part = part_sum_lst[0], part_sum_lst[0]  # 최소값,최대값의 초기값을 설정해둠
#     for i in range(N-M+1):
#         if part_sum_lst[i] < min_part:      # 최소값
#             min_part = part_sum_lst[i]
#
#         elif part_sum_lst[i] > max_part:    # 최대값
#             max_part = part_sum_lst[i]
#
#     print(f'#{test_case} {max_part - min_part}')



'''
슬라이싱을 이용한 짧은 풀이
'''

T = int(input())  # 테스트 케이스 갯수 받기
for tc in range(1, T+1):  # 테스트 케이스 만큼 돌면서
    N, M = map(int, input().split())  # 입력값을 N,M에 넣기
    Num_list = list(map(int, input().split()))  # 숫자 값을 넘버 리스트에 넣기
 
    ans = 0
    for number in Num_list[:M]:
        ans += number
 
    Max_sum = ans
    Min_sum = ans
 
    for i in range(N-M):
        ans -= Num_list[i]
        ans += Num_list[M+i]
 
        if ans < Min_sum:
            Min_sum = ans
        elif ans > Max_sum:
            Max_sum = ans
 
    print(f'#{tc} {Max_sum-Min_sum}')

