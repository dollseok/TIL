'''

1<= N,M <= 8 세로, 가로 => arr[N][M] => arr[y][x]

사각지대 최소 크기

각 자리별로 최대 64개만 확인하면 됨 => 칸수 확인하는 건 쉬움



'''

import copy

n,m = map(int,input().split())

arr = []
cctv = []

for i in range(n):
    data = list(map(int,input().split()))
    arr.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j],j,i])

#     북,동,남,서
dx = [0,1,0,-1]
dy = [-1,0,1,0]

mode = [
    [],
    [[0],[1],[2],[3]], # 1
    [[0,2],[1,3]], # 2
    [[0,1],[1,2],[2,3],[0,3]], # 3
    [[0,1,2],[1,2,3],[0,1,3],[0,2,3]],# 4
    [[0,1,2,3]] # 5
    ]

# 감시하는 함수
def fill(board,mode,x,y):
    for i in mode:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                break

            if board[ny][nx] == 6:
                break
            elif board[ny][nx] == 0:
                board[ny][nx] = -1


# 각 숫자 별로 방향에 대한 함수를 주고
def backtracking(depth,board):
    global result
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += board[i].count(0)

        result = min(count,result)
        return

    tmp = copy.deepcopy(board)
    cctv_num,x,y = cctv[depth]
    for i in mode[cctv_num]:
        fill(tmp,i,x,y)
        backtracking(depth+1,tmp)
        tmp = copy.deepcopy(board)

result = 10e9
backtracking(0,arr)

print(result)