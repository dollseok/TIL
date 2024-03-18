'''
무조건 레버쪽으로 간다
이후 리셋
그리고 다시 시작
최대 100*100
bfs로 찾는게 빠를듯
'''

from collections import deque

def solution(maps):
    answer = 0
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    n = len(maps)
    m = len(maps[0])
    
    leverVisited = [[False]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    leverQ = deque()
    q = deque()
   
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i,j)
                leverVisited[i][j] = True    
                leverQ.append((i,j,0))

    
    while leverQ and not q:
        x,y,cnt = leverQ.popleft()    
        for i in range(4):
            cx, cy = x + dx[i], y + dy[i]
            if 0 <= cx < n and 0 <= cy < m:
                if (maps[cx][cy] == 'O' or maps[cx][cy] == 'E') and not leverVisited[cx][cy]:
                    leverVisited[cx][cy] = True
                    leverQ.append((cx,cy,cnt + 1))
                    
                # 만약에 cx,cy 가 레버 도착
                if maps[cx][cy] == 'L':    
                    q.append((cx,cy,cnt + 1))
                    visited[cx][cy] = True
                    break
    
    while q:    
        x,y,cnt = q.popleft()
        for i in range(4):
            cx, cy = x + dx[i], y + dy[i]
            if 0 <= cx < n and 0 <= cy < m:
                if (maps[cx][cy] == 'O' or maps[cx][cy] == 'S') and not visited[cx][cy]:
                    visited[cx][cy] = True
                    q.append((cx,cy,cnt+1))
                    
                # 만약에 cx,cy 가 끝에 도착
                if maps[cx][cy] == 'E':    
                    answer = cnt+1
                    break
        
        if answer != 0:
            break
    
    if answer == 0:
        answer = -1
    
    return answer