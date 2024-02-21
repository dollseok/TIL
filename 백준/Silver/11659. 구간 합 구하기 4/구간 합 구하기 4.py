'''
11659번
누적합 문제 -> prefix를 먼저 만들고 그 후에 계산
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

arr = list(map(int,input().split()))
prefix = [0]

before = 0
for i in range(n):
    before += arr[i]
    prefix.append(before)

for _ in range(m):
    i,j = map(int,input().split())
    print(prefix[j]-prefix[i-1])