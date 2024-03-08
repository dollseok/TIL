'''
11404번 플로이드
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
arr = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    arr[i][i] = 0

for _ in range(m):
    s,e,pay = map(int,input().split())
    arr[s][e] = min(pay, arr[s][e])

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            arr[a][b] = min(arr[a][b], arr[a][i] + arr[i][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j] == INF:
            arr[i][j] = 0

for i in range(1,n+1):
    print(*arr[i][1:])