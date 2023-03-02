#BAELJOON 1018번 체스판 다시 칠하기

'''
8x8의 체스판을 제작하려고한다
일부를 잘라서 사용하는데 그중에 가장 적게 색칠해서 만들수 있는 체스판의 색칠 개수를 구하는 것

처음엔 전체를 다 체스로 만드는 줄 알았는데 일부사용이였던 것
8x8의 체스판 chess1, chess2를 미리 만들어두고 비교

다르면 색칠을 하는 방식
'''

import sys
sys.stdin = open('input.txt','r')

import sys
input = sys.stdin.readline

N, M = map(int, input().split())               # MxN의 보드
arr = [list(input()) for i in range(N)]        # 보드
chess1 = [[0]*8 for _ in range(8)]
chess2 = [[0]*8 for _ in range(8)]

# [1] 체스판 두개 제작
for i in range(8):
    for j in range(8):
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                chess1[i][j] = 'W'
                chess2[i][j] = 'B'
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                chess1[i][j] = 'B'
                chess2[i][j] = 'W'

res = 999999
# [2] 일부씩 잘라서 몇개씩 칠하는지 확인하고 최소값인지 확인
for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for di in range(8):
            for dj in range(8):
                if arr[i+di][j+dj] != chess1[di][dj]:
                    cnt1 += 1
                if arr[i+di][j+dj] != chess2[di][dj]:
                    cnt2 += 1

        mn = min([cnt1, cnt2])

        if res > mn:
            res = mn

print(res)
