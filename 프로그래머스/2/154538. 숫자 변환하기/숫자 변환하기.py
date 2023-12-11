"""
1. 아이디어
bfs로 해서 한단계에 세가지 계산을 다 해본다.
후에 결과에서 y가 나온다면 끝
아니면 다음 단계 진행

3. 필요한 것

"""

from collections import deque
deq = deque()


def bfs(s,e,n):
    q = deque()
    q.append((e, 0))

    while q:
        y,cnt = q.popleft()

        if y == s:
            return cnt
        if y%3 == 0 and y//3 >= s and y - y//3 > n:
            q.append((y//3, cnt + 1))
        if y%2 == 0 and y//2 >= s and y-y//2 > n:
            q.append((y//2, cnt + 1))
        if y - n >= s:
            q.append((y-n, cnt + 1))

    return -1

def solution(x, y, n):
    answer = bfs(x,y,n)
    return answer
