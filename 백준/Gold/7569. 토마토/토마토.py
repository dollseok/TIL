'''
7569번 토마토


'''

from collections import deque

m,n,h = map(int,input().split())
arr = [[] for _ in range(h)]

dh = [0,0,0,0,1,-1]
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]



for i in range(h):
    for _ in range(n):
        arr[i].append(list(map(int,input().split())))

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([k,j,i,0]) # x,y,h 좌표와 현재 일수

result = 0
while q:
    cx,cy,ch,cday = q.popleft()
    result = max(cday,result)
    for i in range(6):
        tx,ty,th = cx+dx[i], cy+dy[i], ch+dh[i]
        if 0 <= tx < m and 0 <= ty < n and 0 <= th < h:
            if arr[th][ty][tx] == 0:
                q.append([tx,ty,th,cday+1])
                arr[th][ty][tx] = 1

for i in range(h):
    for j in range(n):
        if 0 in arr[i][j]:
            result = -1


print(result)
