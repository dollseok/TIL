'''
14500번 테트로미노

4개 연결되어있는 수중에 최대값을 찾아라

각자리수에 다섯가지의 경우의 수

dfs
깊이 4까지 해서 최종값 리턴

가로 * 세로 * 한칸당 dfs

dfs 바로전 들어온 방향 반대 제외 3방향 -> 4*3*3

500*500*4*3*3
-> 2초 가능할 것으로 보임
'''

n,m = map(int,input().split())
arr = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
result = 0
visited = [[False] * m for _ in range(n)]


for _ in range(n):
    arr.append(list(map(int,input().split())))

def dfs(x,y,depth,sum_):
    global result

    if depth == 4:
        result = max(sum_,result)
        return

    for i in range(4):
        cx,cy = x + dx[i], y + dy[i]
        if 0 <= cx < n and 0 <= cy < m:
            if not visited[cx][cy]:
                visited[cx][cy] = True
                dfs(cx,cy,depth + 1, sum_+arr[cx][cy])
                visited[cx][cy] = False

# 법규 모양의 것 -> 4가지 경우의 수
def tri_dfs(x,y):
    global result
    dr = [[(1,0),(-1,0),(0,1)],
          [(1,0),(-1,0),(0,-1)],
          [(0,1),(0,-1),(1,0)],
          [(0,1),(0,-1),(-1,0)]]

    for i in range(4):
        sum_ = arr[x][y]
        cnt = 0
        for dx,dy in dr[i]:
            cx = x + dx
            cy = y + dy
            if 0 <= cx < n and 0 <= cy < m:
                sum_ += arr[cx][cy]
                cnt += 1

        if cnt == 3:
            result = max(result,sum_)


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,arr[i][j])
        tri_dfs(i,j)
        visited[i][j] = False

print(result)