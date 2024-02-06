from collections import deque

n,m = map(int,input().split())

target_list = list(map(int,input().split()))
queue = deque()

for i in range(1,n+1):
    queue.append(i)

result = 0

def left(q, cnt):
    global result
    result += cnt
    for _ in range(cnt):
        q.append(q.popleft())
    return q

def right(q,cnt):
    global result
    result += cnt
    for _ in range(cnt):
        q.appendleft(q.pop())
    return q

for target in target_list:
    idx = queue.index(target)
    l = len(queue)
    if idx < l-idx:
        queue = left(queue,idx)
    else:
        queue = right(queue,l-idx)

    queue.popleft()

print(result)