# SWEA 1949번 모의 SW 역량 테스트 등산로 조성

'''
틀린 이유:
K가 커지는 경우 돌아왔던 곳을 다시 돌아오는 경우가 생긴다 -> 그래서 visited를 추가해줌

봉우리에서 높이가 낮은 방향으로 등산로 제작하는 것
K 높이만큼 단 한 번 깎아 낼 수 있다
'''

# import sys
# sys.stdin = open('input.txt','r')

def backtrack(si,sj,cnt):
    global usage_K, ans

    if cnt > ans:
        ans = cnt

    dr = [(1,0),(0,1),(-1,0),(0,-1)]

    for di, dj in dr:                                      # 네방향 확인
        if 0 <= si + di < N and 0 <= sj + dj < N:          # 범위 안
            if arr[si][sj] > arr[si+di][sj+dj]:            # 이동할 위치의 높이가 현재위치보다 낮다면
                visited[si + di][sj + dj] = 1              # 방문 표시
                backtrack(si+di,sj+dj,cnt+1)               # 백트래킹
                visited[si + di][sj + dj] = 0              # 다시 비방문 표시

            else:
                # 차이가 K보다 작고, 이동하려는 방향에 방문을 하지 않았었고, K를 사용 전이라면
                if arr[si+di][sj+dj] - arr[si][sj] < K and visited[si+di][sj+dj] == 0 and usage_K == 1:
                    usage_K = 0                               # K 사용했다는 표시
                    temp = arr[si + di][sj + dj]              # 임시변수에 바뀌기 전의 값을 저장
                    arr[si + di][sj + dj] = arr[si][sj] - 1   # 높이를 깎아줌
                    visited[si + di][sj + dj] = 1             # 이동 방향에 방문 표시
                    backtrack(si + di, sj + dj, cnt + 1)      # 백트래킹
                    visited[si + di][sj + dj] = 0             # 다시 미방문 표시
                    arr[si + di][sj + dj] = temp              # 임시변수를 다시 넣어줌
                    usage_K = 1                               # K 사용했다는 표시 해제

                    # 원래는 K 값에 따라 변화될거라 생각했지만 바로 전의 높은 높이에서 -1 한 값만 되면 이동 가능
                    # for i in range(arr[si+di][sj+dj] - arr[si][sj]+1,K+1):
                    #     arr[si + di][sj + dj] = arr[si + di][sj + dj] - i
                    #     visited[si + di][sj + dj] = 1
                    #     backtrack(si+di,sj+dj,cnt+1)
                    #     visited[si + di][sj + dj] = 0
                    #     arr[si + di][sj + dj] = arr[si + di][sj + dj] + i

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    top = 0
    top_list = []

    # 봉우리 높이
    for i in range(N):
        top = max(max(arr[i]),top)

    # 봉우리의 위치
    for i in range(N):
        for j in range(N):
            if arr[i][j] == top:
                top_list.append((i,j))

    # 높이차이가 K 이하라면 진행 아니라면 패스
    # 공사 기회는 1번

    usage_K = 1     # K가 사용되어진 것을 확인하는 변수
    ans = 0
    visited = [[0]*N for _ in range(N)]    # 지나온 자리를 체크한다

    for si,sj in top_list:
        visited[si][sj] = 1
        backtrack(si,sj,1)
        visited[si][sj] = 0
    print(f'#{test_case}', ans)
