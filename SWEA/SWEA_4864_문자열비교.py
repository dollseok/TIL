# SWEA 4864번 문자열 비교
# in 연산자를 쓰면 금방 풀지만 for 문으로 풀어보아라
# 슬라이싱 연산자를 마지막에 쓰면 좋을 듯

# 슬라이싱 연산자를 이용한 풀이

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
    check = input()               # 첫번째 문자열은 들어있는지 확인할 문자열이라 덩어리로 받는다
    target = input()
    N = my_len(check)             # 길이로 몇개씩 돌려야할지 확인한다.
    M = my_len(target)

    for i in range(M-N+1):   # N의 길이씩 만큼 비교를 하기 때문에 기준점을 N-M+1까지로 한다.  (범위 설정 주의)
        if check == target[i:i+N]:
            res = 1
            break
        else:
            res = 0

    print(f'#{test_case} {res}')



# 나의 풀이

# import sys
# sys.stdin = open("input.txt", "r")
#
# # 길이를 확인하는 함수
# def my_len(a):
#     cnt = 0
#     for _ in list(a):
#         cnt += 1
#     return cnt
#
# T = int(input())
# for test_case in range(1, T+1):
#     check = input()               # 첫번째 문자열은 들어있는지 확인할 문자열이라 덩어리로 받는다
#     target = input()
#     target_list = list(target)    # 잘라서 일부씩 확인해야하기 때문에 리스트로 받는다
#     N = my_len(check)             # 길이로 몇개씩 돌려야할지 확인한다.
#     M = my_len(target)
#
#     # if N == M:
#     #     if target == check:
#     #         res = 1
#     #     else:
#     #         res = 0
#     #
#     # else:
#     for i in range(M-N+1):   # N의 길이씩 만큼 비교를 하기 때문에 기준점을 N-M+1까지로 한다.  (범위 설정 주의)
#         target_part = []     # 타겟 대상을 일부씩 받을 리스트
#         for j in range(N):
#             target_part.append(target_list[i+j])    # N의 길이만큼씩 비교를 한다    # 슬라이싱 연산자를 사용하면 좋을 듯
#         n_target = ''.join(target_part)        # 덩어리로 비교를 하기 때문에 join을 사용
#
#         if check == n_target:     # 같은 것이 있을 때
#             res = 1
#             break                 # for문을 마쳐야 있다는 것을 확인하고 끝날 수 있다.
#         else:
#             res = 0
#
#     print(f'#{test_case} {res}')


