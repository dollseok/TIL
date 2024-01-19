'''
1520번 내리막길

0,0 -> N-1,M-1까지 가는게 목표
'''

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [[-1]*m for _ in range(n)] # 여기까지 오는데 필요한 개수(메모이제이션)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    road = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if arr[y][x] > arr[ny][nx]:
                road += dfs(nx,ny)

    dp[y][x] = road
    # for i in range(n):
    #     print(dp[i])
    # print('00000000000000000000')

    return dp[y][x]

print(dfs(0,0))