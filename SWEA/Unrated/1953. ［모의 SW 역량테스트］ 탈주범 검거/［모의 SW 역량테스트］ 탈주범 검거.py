#SWEA모의 SW 역략테스트 1953번 탈주범 검거

'''
BFS 문제에 가까움
'''

di = [[-1, 0], [1, 0], [0, -1], [0, 1]]    # 상 하 좌 우

def connect(k):
    if k == 0:     # 0 - 1 이면 연결
        return 1
    elif k == 1:   # 1 - 0 이면 연결
        return 0
    elif k == 2:   # 2 - 3 이면 연결
        return 3
    elif k == 3:   # 3 - 2 이면 연결
        return 2


def passage(n):              # 연결 통로 확인
    k_list = []
    if n == 1:               # 상 하 좌 우
        k_list = [0,1,2,3]
    elif n == 2:             # 상 하
        k_list = [0, 1]
    elif n == 3:             # 좌 우
        k_list = [2, 3]
    elif n == 4:             # 상 우
        k_list = [0, 3]
    elif n == 5:             # 하 우
        k_list = [1, 3]
    elif n == 6:             # 하 좌
        k_list = [1, 2]
    elif n == 7:             # 상 좌
        k_list = [0, 2]
    return k_list

T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int,input().split())
    # N : 세로크기, M : 가로크기, R : 맨홀 세로 좌표, C : 맨홀 가로좌표, L : 도망친 시간

    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    arr = [[0]*(M+2)] + arr + [[0]*(M+2)]
    visited = [[0]*(M+2) for _ in range(N+2)]

    si, sj = R+1, C+1         # 시작 위치 좌표

    # 시작점 세팅
    queue = [(si, sj)]        # 첫 시작점에 큐 추가
    visited[si][sj] = 1       # 방문 체크
    cnt = 1                   # 개수 1개부터 시작

    while queue:                        # 큐가 있을 동안 반복
        ti, tj = queue.pop(0)           # dequeue해서 가져옴
        if visited[ti][tj] == L:        # 시간이 되면 break
            break

        for k in passage(arr[ti][tj]):                                             # 이어진 통로에 대한 k에 대해서
            if connect(k) in passage(arr[ti + di[k][0]][tj + di[k][1]]):           # connect를 써서 변환시켜주면 건너편에 있는 것과 연결되어있는지 확인 가능
                if visited[ti + di[k][0]][tj + di[k][1]] == 0:                     # 방문하지 않았다면
                    queue.append((ti + di[k][0], tj + di[k][1]))                   # queue에 추가
                    visited[ti + di[k][0]][tj + di[k][1]] = visited[ti][tj] + 1    # 방문 체크
                    cnt += 1             # 개수 체크

    print(f'#{test_case}', cnt)
