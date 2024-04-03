'''
11403번 경로찾기

풀이
모든 정점 i->j 가는 길이 존재하는지 확인
n = 최대 100
dfs? => 100*100에 각 자리마다 dfs 돌리기엔 너무 오래 걸린다
bfs => visited로 파악하며 도착한 위치 확인

입력
정점 개수 n
n개 줄에는 그래프의 인접행렬 주어짐

'''

from collections import deque

n = int(input())

graph = [list(map(int,input().split())) for _ in range(n)]

check = [False] * n
result_graph = [[0] * n for _ in range(n)]

for i in range(n):
    visited = [0] * n
    q = deque([i])
    visited_flag = False
    while q:
        current = q.popleft()
        if check[current]:
            result_graph[i] = result_graph[target]
            visited_flag = True
            break

        for target in range(n):
            if graph[current][target] == 1 and visited[target] == 0:
                q.append(target)
                visited[target] = 1

    if not visited_flag:
        result_graph[i] = visited

for i in result_graph:
    print(*i)
