from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
p1,p2 = map(int,input().split())

arr = [[] for _ in range(n+1)]
visited = [0]*(n+1)

m = int(input())

for _ in range(m):
    parent, children = map(int,input().split())
    arr[parent].append(children)
    arr[children].append(parent)

queue = deque()
queue.append(p1)

while queue:
     v = queue.popleft()
     for i in arr[v]:
         if visited[i] == 0:
             visited[i] = visited[v] + 1
             queue.append(i)

if visited[p2] == 0:
    print(-1)
else:
    print(visited[p2])
