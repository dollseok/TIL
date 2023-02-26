#SWEA 문제해결 기본 1220번 magnetic

'''
1 : N극 자성을 가짐 : 아래로
2 : S극 자성을 가짐 : 위로
교착 상태의 개수 확인
arr 세로로 볼것
0을 지우고 위가 1, 아래 2 인 개수 파악 == 교착 상태 개수


'''

import sys
sys.stdin = open("input.txt", "r")

def del0(arr):      # 리스트에서 0을 제거해주는 함수
    new_arr = []
    for i in arr:
        if i != 0:
            new_arr.append(i)
    return new_arr

for test_case in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list,zip(*arr)))     # 세로로 뒤집은 arr

    # print(arr_t)
    cnt = 0
    for i in range(N):
        arr_t[i] = del0(arr_t[i])        # 0을 싹 지운 arr로 새로 만든다.
        # print(arr_t[i])                # [1], [2], [2, 1, 2, 1], [1, 2], [1, 1, 2], [1, 2, 1, 2], [1, 2, 1, 2]
        len_ = len(arr_t[i])
        for j in range(len_ - 1):        # 새로만든 arr의 줄별로 확인
            if arr_t[i][j] == 1:         # 위에부터 확인하는데 1이 나오고 나서
                if arr_t[i][j+1] == 2:   # 2가 나와야 합쳐짐
                    cnt += 1
            # 나머지는 패스

    print(f'#{test_case}', cnt)

