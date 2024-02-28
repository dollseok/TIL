'''
1149번 RGB 거리
dfs
n = 최대 1000

dfs 쓰면 시간 초과

dp 로 풀라고 함

'''

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    # 현재 i 위치에서 그전의 것들을 다 고려했을 때 어떤 것을 골랐을 때 최소값인가
    arr[i][0] = min(arr[i-1][1],arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0],arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0],arr[i-1][1]) + arr[i][2]

print(min(arr[n-1]))