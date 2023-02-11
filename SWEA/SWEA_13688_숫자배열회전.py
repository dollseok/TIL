# SWEA 13688번 숫자 배열 회전

import sys
sys.stdin = open("input.txt", "r")


# 돌린 것을 다시 돌리는 풀이 (함수 정의 사용)

def rotate90(arr,n):
    newarr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newarr[i][j] = arr[(n - 1) - j][i]
    return newarr

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(input().split() for _ in range(n))

    arr90 = rotate90(arr, n)
    arr180 = rotate90(arr90, n)
    arr270 = rotate90(arr180, n)

    print(f'#{test_case}')
    for a, b, c in zip(arr90,arr180,arr270):
        print(''.join(a), ''.join(b), ''.join(c))




# 나의 풀이

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(input().split() for _ in range(n))

    new_arr90 = list([0] * n for _ in range(n))
    new_arr180 = list([0] * n for _ in range(n))
    new_arr270 = list([0] * n for _ in range(n))

    for i in range(n):
        for j in range(n):
            new_arr90[i][j] = arr[(n-1)-j][i]
            new_arr180[i][j] = arr[(n-1)-i][(n-1)-j]
            new_arr270[i][j] = arr[j][(n-1)-i]

    # 다양한 프린트 방법

    print(f'#{test_case}')
    # for i in range(n):
    #     print(''.join(new_arr90[i]) + ' ' + ''.join(new_arr180[i])+ ' ' +''.join(new_arr270[i]))

    # for i in range(n):
    #     print(''.join(new_arr90[i]), ''.join(new_arr180[i]), ''.join(new_arr270[i]))

    for a, b, c in zip(new_arr90, new_arr180, new_arr270):
        # a,b,c 각각에 하나씩 받음
        # [['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3']]
        # [['9', '8', '7'], ['6', '5', '4'], ['3', '2', '1']]
        # [['3', '6', '9'], ['2', '5', '8'], ['1', '4', '7']]
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')


