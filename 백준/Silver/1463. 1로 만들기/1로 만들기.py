'''
3가지의 연산
1. X가 3으로 나누어 떨어지면 3으로 나눔
2. X가 2로 나누어 떨어지면 2로 나눔
3. 1을 뺀다

연산 횟수의 최소값
10**6 보다 작거나 같은 N
'''

N = int(input())
dp = [0]*(N+1)

for i in range(2,N+1):
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)


print(dp[N])