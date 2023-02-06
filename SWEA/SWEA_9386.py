# SWEA 9386 연속한 1의 개수
#

import sys
sys.stdin = open("input.txt", "r")

# split('0')으로 1의 덩어리를 만들어서 그중가장 큰 값의 길이를 구하는 방식으로 풀어도 가능할 것 같음

# 나의 풀이
T = int(input())
for test_case in range(1, T+1):
    N = int(input())    # N = 0과 1로 이루어진 수열의 길이
    N_list = list(str(input()))    # 문자열로 나누어서 받아주었습니다.
    # 0011001110
    # print(N_list) # ['0','0','1','1','0','0','1','1','1,'0']
    cnt_max = 0     # 1이 없는 경우는 0 이므로 기본 최대값을 0으로 설정했습니다.

    for i in range(N):
        if N_list[i] == '0':    # list에서 0을 만나면  cnt = 0
            cnt = 0             # cnt = 0 으로 리셋
        elif N_list[i] == '1':  # list에서 1이라면
            cnt += 1            # cnt 에  1 추가
            if cnt > cnt_max:   # cnt가 최대값인지 확인
                cnt_max = cnt

    print(f'#{test_case} {cnt_max}')


# 강의 풀이
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input()))
#     ans = cnt = 0
#     for i in range(N):
#         if lst[i] == 0:
#             cnt = 0
#         else:
#             cnt += 1
#             if ans < cnt:
#                 ans = cnt
#
#     print(f'#{test_case}', ans)
















