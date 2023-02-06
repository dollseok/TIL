# SWEA 16268 풍선팡 2

'''
NxM 크기의 격자판
상하좌우의 풍선이 터짐
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    '''
    [[3, 4, 1, 2, 3], 
     [3, 4, 1, 3, 2], 
     [2, 3, 2, 4, 1], 
     [1, 4, 4, 1, 3], 
     [2, 2, 3, 4, 4]]
    '''
    print(arr)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    tot_max = 0

    for x in range(N):   # arr 순환하면서 체크
        for y in range(M):
            tot = 0
            tot += arr[x][y]    # 자기 자신을 더해줘야함
            for k in range(4):  # k의 방향은 4방향 상하좌우
                cx = x + dx[k]
                cy = y + dy[k]
                if 0 <= cx < N and 0 <= cy < M:   # 칸을 넘어가는 경우 제외
                    tot += arr[cx][cy]

            if tot_max < tot:
                tot_max = tot

    print(f'#{test_case} {tot_max}')

