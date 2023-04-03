# SWEA 5247번 연산

'''
자연수 N을 몇번의 연산을 통해 다른 자연수 M을 만드려한다

사용 연산 : +1 -1, *2 ,-10
최소 몇번의 연산 필요?

연산 중간 결과도 백만 이하
'''

from collections import deque


def bfs(start, end):
    queue = [(start, 0)]
    queue = deque(queue)

    while queue:
        tmp = queue.popleft()

        if visited[tmp[0]] == 0:
            visited[tmp[0]] = 1
            cnt = tmp[1] + 1
            if end in (tmp[0] * 2, tmp[0] + 1, tmp[0] - 1, tmp[0] - 10):
                return cnt

            if tmp[0] * 2 <= 1000000 and visited[tmp[0] * 2] != 1:
                queue.append((tmp[0] * 2, cnt))
            if tmp[0] + 1 <= 1000000 and visited[tmp[0] + 1] != 1:
                queue.append((tmp[0] + 1, cnt))
            if tmp[0] - 1 > 0 and visited[tmp[0] - 1] != 1:
                queue.append((tmp[0] - 1, cnt))
            if tmp[0] - 10 > 0 and visited[tmp[0] - 10] != 1:
                queue.append((tmp[0] - 10, cnt))


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    print(f'#{test_case}', bfs(N, M))