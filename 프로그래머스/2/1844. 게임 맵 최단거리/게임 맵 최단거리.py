from collections import deque

def solution(maps):
    answer = 0
    print(maps)
    
    n = len(maps) - 1 # 세로축 y
    m = len(maps[0]) - 1 # 가로축 x
    
    distance = [[0]*(m+1) for i in range(n+1)]
    print(distance)
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    q = deque([[0,0]])
    distance[0][0] = 1
    while q:
        sx,sy = q.popleft()
        for i in range(4):
            if (0 <= sx + dx[i] <= m and 0 <= sy+dy[i] <= n): # 범위 안에 있을 때
                tx = sx + dx[i]
                ty = sy + dy[i]
                if maps[ty][tx] == 1:
                    # 방문하지 않음 or 방문했는데 지금 온길이 짧은길
                    if distance[ty][tx] == 0 or distance[ty][tx] > distance[sy][sx] + 1: 
                        q.append([tx,ty])   
                        distance[ty][tx] = distance[sy][sx] + 1
    
    if distance[n][m] == 0:
        answer = -1
    else:
        answer = distance[n][m]

    return answer