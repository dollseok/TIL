#SWEA 1216번 회문2

import sys
sys.stdin = open("input.txt", "r")


# palindrome인지 확인
def is_palindrome(list):

    if list == list[::-1]:
        return True

# 양끝이 같은지 확인후 palindrome인지 확인하는 함수
def check(list):

    if list[0] == list[-1]:
        if is_palindrome(list):
            return list

for _ in range(10):
    test_case = int(input())
    arr = list(input() for _ in range(100))  # 가로
    arr_t = list(map(list, zip(*arr)))       # 세로
    mx = 0

    for i in range(100):
        for j in range(100):
            for k in range(99, j, -1):       # 역방향에서부터 확인
                line_w = arr[i][j:k+1]
                line_l = arr_t[i][j:k+1]

                if check(line_w):
                    if mx < len(check(line_w)):
                        mx = len(check(line_w))

                if check(line_l):
                    if mx < len(check(line_l)):
                        mx = len(check(line_l))
                    break                     # 가장 긴곳에서 확인이 되면 끝내도됨(최대값이라)

    print(f'#{test_case} {mx}')