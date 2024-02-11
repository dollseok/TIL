from collections import deque

x,k = map(int, input().split())

cnt = [0]*100001

visited = deque([x])
cnt[x] = 1

while visited:
    p = visited.popleft()
    if p == k:
        break

    for next in (p-1, p+1, p*2):
        if 0 <= next <= 100000:
            if cnt[next] == 0 or cnt[next] > cnt[p]+1:
                cnt[next] = cnt[p] + 1
                visited.append(next)


print(cnt[p] - 1)