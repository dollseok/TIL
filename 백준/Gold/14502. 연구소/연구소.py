import sys
input = sys.stdin.readline
from collections import deque
import copy

n,m = map(int, input().split())

lab = []
for _ in range(n):
    lab.append(list(map(int,input().split())))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

result = 0

def count_empty(graph):
    global result

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1

    result = max(cnt,result)



def bfs():
    queue = deque()
    tmp_lab = copy.deepcopy(lab)

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp_lab[nx][ny] == 0:
                    tmp_lab[nx][ny] = 2
                    queue.append((nx,ny))

    count_empty(tmp_lab)


def make_wall(cnt):

    if cnt == 3:
        bfs() # 바이러스 퍼뜨리기
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                make_wall(cnt+1)
                lab[i][j] = 0


make_wall(0)

print(result)