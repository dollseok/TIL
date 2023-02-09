#SWEA 1215번 회문1

import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())    # 회문의 길이
    arr = list(input() for _ in range(8))
    cnt = 0

    for i in range(8):
        width = arr[i]    # 가로줄
        length = ''.join(arr[j][i] for j in range(8))    # 세로줄

        for i in range(8-N+1):
            palindrome_w = width[i:i+N]    # 가로줄에서 N 길이로 자른 일부
            palindrome_l = length[i:i+N]   # 세로줄에서 N 길이로 자른 일부
            if palindrome_w == palindrome_w[::-1]:    # 뒤집었을 때 같으면 cnt +1
                cnt += 1

            if palindrome_l == palindrome_l[::-1]:    # 뒤집었을 때 같으면 cnt +1
                cnt += 1

    print(f'#{test_case} {cnt}')