# SWEA 1220번 Magnetic

# import sys
# sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1,T+1):
    N = int(input())

    # [1] 함수를 이용해서 푸는 법
    arr = [list(input().split()) for _ in range(N)]
    arr_t = list(map(list,zip(*arr)))
    cnt = 0

    for i in arr_t:
        cnt += ''.join(i).replace('0','').count('12')     # 0을 빈칸으로 대체하고 '12'를 세면 붙은 것의 개수를 알 수 있다.

    print(f'#{test_case}', cnt)

    # [2] 2차원 배열 순회를 통해 푸는 법
    # arr = [list(input().split()) for _ in range(N)]
    # arr_t = list(map(list,zip(*arr)))
    # cnt = 0
    #
    # for i in range(N):
    #     res = ''
    #     for j in range(N):
    #         if arr_t[i][j] != '0':      # 0이 아닌 것은
    #             res += arr_t[i][j]      # res문자열에 추가
    #     cnt += res.count('12')          # '12'의 개수를 세서 붙은 것의 개수 확인
    #
    # print(f'#{test_case}', cnt)