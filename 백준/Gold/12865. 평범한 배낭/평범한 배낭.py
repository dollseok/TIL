'''
평범한 배낭

n개의 물건, 무게 w , 가치 v를 가짐
최대 k 만큼의 무게를 넣을 수 있는 배낭

'''

n,k = map(int,input().split())

ls = [list(map(int,input().split())) for _ in range(n)]

dp = [[-1] * 100010 for _ in range(n)] # 각 무게별 최대 가치

def recur(cur,weight):
    if weight > k:
        return -9999999999999999

    if cur == n:
        return 0

    if dp[cur][weight] != -1:
        return dp[cur][weight]

    dp[cur][weight] = max(recur(cur+1,weight + ls[cur][0]) + ls[cur][1], recur(cur+1,weight))
    return dp[cur][weight]

print(recur(0,0))