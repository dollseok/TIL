#Baekjoon 1260번 DFS와 BFS
'''
https://www.acmicpc.net/problem/1260
'''

import sys
sys.stdin = open("input.txt", "r")

import sys
input = sys.stdin.readline

def BFS(adjL,start):
    res = []
    visited = [0] * (N + 1)
    q = [start]
    visited[start] = 1
    res.append(start)

    while q:
        t = q.pop(0)
        for i in adjL[t]:
            if visited[i] == 0:
                q.append(i)
                res.append(i)
                visited[i] = visited[t] + 1

    return res

def DFS(adjL,V):
    res = []
    visited = [0] * (N+1)
    stack = []
    visited[V] = 1
    res.append(V)
    v = V

    while True:
        for i in adjL[v]:
            if visited[i] == 0:   # 방문하지 않았다면
                stack.append(v)
                v = i
                stack.append(v)
                visited[v] = 1
                res.append(v)
                break

        else:
            if stack:
                v = stack.pop()
            else:
                return res

N,M,V = map(int, input().split())
adjL = [[] for _ in range(N+1)]
visited = [[0]*(N+1)]
for i in range(M):
    v1, v2 = map(int,input().split())
    adjL[v1].append(v2)
    adjL[v2].append(v1)

for i in range(len(adjL)):
    adjL[i] = sorted(adjL[i])


DFS_res = DFS(adjL,V)
BFS_res = BFS(adjL,V)

print(*DFS_res)
print(*BFS_res)
