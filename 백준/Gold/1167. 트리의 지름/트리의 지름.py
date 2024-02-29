'''
트리의 지름

3 1 2 4 3 -1

3번 정점은 1과 거리가 2인 간선, 4와 거리가 3인 간선

-1 끝
'''
import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

# 트리 생성
for _ in range(n):
    data = list(map(int,input().split()))
    v = data[0]
    for i in range(1,len(data)//2):
        # 각 인덱스 2*i-1, 2*i
        tree[v].append([data[2 * i - 1], data[2 * i]]) # 정점, 거리

def dfs(v,cnt):
    global result
    for connect in tree[v]:
        vertex, edge = connect
        if visited[vertex] == -1:
            visited[vertex] = cnt+edge
            dfs(vertex, cnt + edge)

# 1부터 시작했을 때 가장 멀리 있는 노드를 찾는다
visited = [-1]*(n+1)
visited[1] = 0
dfs(1,0)

# 가장 먼 노드 부터 시작해서 거기서부터 다시 가장 먼 노드를 찾는다 -> 이때 트리의 지름(가장 먼 거리)
far_node = visited.index(max(visited))
visited = [-1]*(n+1)
visited[far_node] = 0
dfs(far_node,0)


print(max(visited))

