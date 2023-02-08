#SWEA 1210번 Ladder1

import sys
sys.stdin = open("input.txt", "r")


for i in range(10):
    Test_case = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    start_i = 99
    start_j = arr[start_i].index(2)

    while start_i != 0:
        if arr[start_i][start_j - 1] == 1:
            while arr[start_i][start_j-1] != 0:
                start_j -= 1
            start_i -= 1
        elif arr[start_i][start_j + 1] == 1:
            while arr[start_i][start_j + 1] != 0:
                start_j += 1
            start_i -= 1
        else :
           start_i -= 1

    print(f'#{Test_case} {start_j-1}')


