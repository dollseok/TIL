from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    visited = [False]*n
    cnt = 0
    for i in range(n):
        q = deque()
        q.append(i)
        if not visited[i]:
            visited[i] = True
            while q:
                current = q.popleft()
                if not visited[arr[current]-1]:
                    target = arr[current] -1
                    q.append(target)
                    visited[target] = True
            cnt += 1
        
    print(cnt)