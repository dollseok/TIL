'''
지역 높이 정보
2차원 배열의 형태 해당 지점 높이를 표현하는 자연수

장마철 비의 양에 따른 최저점부터 최고점까지 안전영역의 개수 계산
'''

from collections import deque

n = int(input())
arr = []
min_height = 101
max_height = 1
for i in range(n):
    l = list(map(int,input().split()))
    min_height = min(min(l),min_height)
    max_height = max(max(l),max_height)
    arr.append(l)


dx = [0,1,0,-1]
dy = [1,0,-1,0]

result = 0

for h in range(min_height-1,max_height+1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            si, sj = i,j
            if arr[sj][si] > h and not visited[sj][si]:
                q = deque()
                q.append((sj,si))
                while q:
                    cj,ci = q.popleft()
                    for t in range(4):
                        tj,ti = cj + dx[t], ci+dy[t]
                        if 0 <= tj < n and 0 <= ti < n and not visited[tj][ti] and arr[tj][ti] > h:
                            q.append((tj,ti))
                            visited[tj][ti] = True
                cnt += 1

    result = max(cnt,result)

print(result)



