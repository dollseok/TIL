import sys
input = sys.stdin.readline

N, M = map(int, input().split())               
arr = [list(input()) for i in range(N)]
chess1 = [[0]*8 for _ in range(8)]
chess2 = [[0]*8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (i % 2 == 0 and j % 2 == 1) or (i % 2 == 1 and j % 2 == 0):
                chess1[i][j] = 'W'
                chess2[i][j] = 'B'
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                chess1[i][j] = 'B'
                chess2[i][j] = 'W'

res = 999999

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