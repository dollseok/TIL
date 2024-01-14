from sys import stdin

from collections import deque

n,m,k,x = map(int,input().split())

# 인덱스가 도시
road = [[] for _ in range(n+1)]
distance = [-1]*(n+1)
distance[x] = 0

for _ in range(m):
    s,e = map(int,stdin.readline().split())
    road[s].append(e)

queue = deque([x])

while queue:
    city = queue.popleft()
    for next_city in road[city]:
        if distance[next_city] == -1:
            distance[next_city] = distance[city] + 1
            queue.append(next_city)

result_cnt = 0
for i in range(n+1):
    if distance[i] == k:
        print(i)
        result_cnt += 1
if result_cnt == 0:
    print(-1)