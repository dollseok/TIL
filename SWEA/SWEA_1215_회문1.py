#SWEA 1215번 회문1
'''
회문의 개수를 구하는 문제

처음 풀었을 때는 가로 세로 따로 구해서 각자 for문을 돌렸음
두번째로 수정했을 때는 for 문 하나에 가로 세로를 동시에 검사하는 코드를 짰음(현재의 코드)

arr를 세로로 돌리는 arr_t를 만들어서 좀 더 보기쉽게 만들어줌
'''


import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    N = int(input())    # 회문의 길이
    arr = list(input() for _ in range(8))
    arr_t = list(map(list,zip(*arr)))
    cnt = 0

    for i in range(8):
        width = arr[i]    # 가로줄
        # length = ''.join(arr[j][i] for j in range(8))    # 세로줄
        length = arr_t[i]

        for i in range(8-N+1):
            palindrome_w = width[i:i+N]    # 가로줄에서 N 길이로 자른 일부
            palindrome_l = length[i:i+N]   # 세로줄에서 N 길이로 자른 일부
            if palindrome_w == palindrome_w[::-1]:    # 뒤집었을 때 같으면 cnt +1
                cnt += 1

            if palindrome_l == palindrome_l[::-1]:    # 뒤집었을 때 같으면 cnt +1
                cnt += 1

    print(f'#{test_case} {cnt}')