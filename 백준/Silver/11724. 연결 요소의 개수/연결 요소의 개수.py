'''
11724번 연결 요소의 개수

양방향 그래프
무조건 자기자리로 돌아온다
VISITED로 확인
'''

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

visited = [-1] * n

cnt = 0
for _ in range(m):
    u,v = map(int,input().split())
    u,v = u-1, v-1

    if visited[u] == -1 and visited[v] == -1:
        cnt += 1
        visited[u] = cnt
        visited[v] = cnt
    elif visited[u] != -1 and visited[v] != -1:
        big = max(visited[u], visited[v])
        small = min(visited[u], visited[v])
        for i in range(n):
            if visited[i] == big:
                visited[i] = small
    elif visited[u] != -1:
        visited[v] = visited[u]
    elif visited[v] != -1:
        visited[u] = visited[v]

result = 0
for i in visited:
    if i == -1:
        result += 1
        
if result == 0:
    print(len(set(visited)))
else:
    print(len(set(visited)) + result - 1) # -1 은 뺴주고 생각

