'''
2579번 계단 오르기

계단은 한번에 한계단씩 또는 두계단씩 오를 수 있다.
연속된 계단 세계는 안된다
마지막 계단은 반드시 밟아야한다.

계단의 개수는 300이하
점수는 10000점 이하 자연수
0 0 0 0 0 0 0
'''

N = int(input())
data = [int(input()) for _ in range(N)]
dp = [0]*(N)
dp[0] = data[0]

if N == 2:
    dp[1] = data[0]+data[1]
if N >= 3:
    dp[0] = data[0]
    dp[1] = data[0] + data[1]
    dp[2] = max(data[0]+data[2], data[1]+data[2])

    for i in range(3,N):
        dp[i] = max(dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i])

print(dp[-1])


