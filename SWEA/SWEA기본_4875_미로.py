#SWEA 기본 해결 문제 4875번 미로

'''
NxN의 미로에서 출발지(2)에서 도착지(3)까지ㅡ 가는 경로가 존재하는지 확인하는 알고리즘
통로는 0

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())

    maze = [[1] + list(map(int, input())) + [1] for _ in range(N)]  # 좌 우 패딩
    maze = ([[1]*(N+2)] + maze + [[1]*(N+2)])                       # 위 아래 패딩

    visited = [[False]*(N+2) for _ in range(N+2)]

    di = [-1, 1, 0, 0]  # 상 하 좌 우
    dj = [0, 0, -1, 1]

    start_i = 0
    start_j = 0
    # 시작지점 찾기
    for i in range(1, N+1):
        for j in range(1, N+1):
            if maze[i][j] == 2:
                start_i, start_j = i, j
                break

    ci, cj = (start_i, start_j)
    k = 0
    res = 0
    stack = [(start_i, start_j)]                # 첫 시작점을 스택에 추가 시켜둠

    while True:
        for k in range(4):                      # 네방향 탐색
            if maze[ci+di[k]][cj+dj[k]] == 3:   # 3 발견하면 break
                res = 1
                stack.clear()                   # for 문에서 나가는 것이므로 한번 더 while문에서 나가야하기 때문에 stack을 비워준다
                break

            if maze[ci+di[k]][cj+dj[k]] == 0 and not visited[ci+di[k]][cj+dj[k]]:   # 0이거나 방문하지 않았던 곳이라면
                temp = (ci+di[k], cj+dj[k])                                         # 임시 변수에 튜플로 넣어주고
                stack.append(temp)                                                  # stack에 추가

        else:                                   # for-else를 먼저 붙여줘야 for else문으로 붙음
            visited[ci][cj] = True              #
            ci, cj = stack.pop()

        if not stack:
            break

    print(f'#{test_case}', res)




















#     check_i = ci + di[k]
#     check_j = cj + dj[k]
#
#     if maze[check_i][check_j] != 0:
#         k += 1
#         check_i = ci
#         check_j = cj
#         if k == 4:
#             visited[ci][cj] = True
#             ci,cj = stack.pop()
#             k = 0
#     elif maze[check_i][check_j] == 3:
#         res = 1
#         break
#
#     elif maze[check_i][check_j] == 0:
#         if not visited[check_i][check_j]:  # 그 자리 false라면
#             visited[ci][cj] = True
#             stack.append((ci, cj))
#             ci = check_i
#             cj = check_j
#             k = 0
#             continue
#         else:
#             k += 1
#             if k == 4:
#                 visited[ci][cj] = True
#                 ci, cj = stack.pop()
#                 k = 0
#
# print(res)


