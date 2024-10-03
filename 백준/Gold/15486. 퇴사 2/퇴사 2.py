import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]

dp = [-1]*n

def recur(cur): # 현재 cur 일차, 앞으로 최대치의 가격을 고를때, 벌 수 있는 최대 이익

    # 넘어감
    if cur > n:
        return -9999999999999
    # 마지막 날 도착
    if cur == n:
        return 0

    if dp[cur] != -1:
        return dp[cur]

    dp[cur] = max(recur(cur + ls[cur][0])+ls[cur][1], recur(cur+1))
    return dp[cur]

print(recur(0))