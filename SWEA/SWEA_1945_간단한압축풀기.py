#SWEA 1945번 간단한 압축풀기

import sys
sys.stdin = open("input.txt", "r")

'''
이전 풀이
틀린 이유 : replace는 똑같은 것을 그대로 바꿔버린다.
'''

# def my_len(a):
#     cnt = 0
#     for _ in a:
#         cnt += 1
#     return cnt
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     total = ''                 # 전부를 합쳐줄 문자열
#     for _ in range(N):
#         Ci, Ki = input().split()
#
#         total += Ci * int(Ki)  # 곱해서 개수만큼 합쳐줌
#
#     q = my_len(total)//10      # 몫만큼 10줄이 차기 때문에 10개씩 만들어줄 개수 확인
#
#     print(f'#{test_case}')
#     for i in range(q):
#         print(total[0:10])
#         total = total.replace(total[0:10], '')     # 출력된 것들 제외시킴
#     if total != '':
#         print(total)            # 남은 것들 프린트



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cnt = 0
    total = ''                 # 전부를 합쳐줄 문자열
    for _ in range(N):
        Ci, Ki = input().split()
        cnt += int(Ki)

        total += Ci * int(Ki)  # 곱해서 개수만큼 합쳐줌

    q = cnt//10      # 몫만큼 10줄이 차기 때문에 10개씩 만들어줄 개수 확인

    print(f'#{test_case}')
    for i in range(q):
        print(total[i*10:(i*10 + 10)])

    print(total[q*10:cnt+1])    # 10개씩 프린트한 것 끝에서부터 마지막까지 프린트
