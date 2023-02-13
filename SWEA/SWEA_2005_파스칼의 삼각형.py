#SWEA 2005번 파스칼의 삼각형

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    before_lst = []             # 새로 만들어진 리스트를 저장할 리스트를 만든다.
    res = []             # 결과를 모을 리스트
    for i in range(N):
        new_lst = [1]*(i + 1)       # 전체에 1을 넣어둘
        if i >= 2:                  # 행이 2를 넘어갈 때
            for j in range(1, i):   # 위에서 합친 것을 들어갈 위치 j
                new_lst[j] = before_lst[j-1] + before_lst[j]     # 위 리스트에서 더해서 넣어준다

        before_lst = new_lst        # 직전 리스트와 계속 비교해야하기 때문에 그전 리스트에 new lst를 넣어준다.
        res.append(new_lst)

    print(f'#{test_case}')
    for l in res:
        print(*l)



# 프린트 방법이 헷갈렷었음

# T = int(input())
# for test_case in range(1, T+1):
#     print(f'#{test_case}')
#     N = int(input())
#     lst = []
#     for i in range(N):
#         new_lst = [1]*(i + 1)
#         if i >= 2:
#             for j in range(1, i):
#                 new_lst[j] = lst[j-1] + lst[j]
#
#         lst = new_lst
#         print(*lst)