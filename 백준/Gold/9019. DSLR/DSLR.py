'''
9019번 DSLR

6초

DSLR을 이용하는 간단한 계산기
a,b 는 0이상 10000미만 -> 최대 4자리
'''
from collections import deque

t = int(input())

for _ in range(t):
    a,b = input().split()
    visited = [False] * 10000

    check = deque()
    check.append([a,''])
    while check:
        num,command = check.popleft()
        num = int(num)

        if num == int(b):
            print(command)
            break

        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            check.append([d, command+'D'])
        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            check.append([s, command+'S'])
        l = num // 1000 + (num % 1000 )* 10
        if not visited[l]:
            visited[l] = True
            check.append([l, command+'L'])
        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            check.append([r, command+'R'])

