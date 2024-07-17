'''
포도주 잔을 선택하면 그 잔에 들어있는 포도주 모두 마셔야함
연속으로 놓인 3잔을 모두 마실 수 없음

경우의 수가 3가지

0 0 0 0 0 ...
o o x
o x o
x o o
 

'''

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0]*n

dp[0] = arr[0]

if n > 1:
    dp[1] = arr[0]+arr[1]

if n > 2:
    dp[2] = max(arr[2] + arr[1], arr[2] + arr[0], dp[1])

if n > 3:
    for i in range(3,n):
        dp[i] = max(dp[i-1], dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])

print(dp[n-1])