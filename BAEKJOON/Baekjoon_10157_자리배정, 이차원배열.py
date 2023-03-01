# baekjoon 10157번 자리배정

'''
CxR격자형 배치
좌석 번호는 격자의 좌표 x,y   아래에서 위 방향으로

첫 좌표를 설정을 안해줘서 틀린 것

반례로
5 5
1
'''

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

Y, X = map(int,input().split())             # 7가로 6 세로
G = int(input())                            # 도착 지점

dr = [[0, 1], [1, 0], [0, -1], [-1, 0]]     # 오른쪽 아래 왼쪽 위
arr = [[0]*X for _ in range(Y)]
visited = [[0]*X for _ in range(Y)]

ti,tj = (0,0)             # 시작 좌표   (문제에서는 위치를 다르게 줬지만 내가 돌려주었음)
visited[ti][tj] = 1       # 방문했음 표시
seat = 1                  # 자리 번호 1부터 시작
arr[ti][tj] = seat        # arr에 자리 번호 채워줌
k = 0

while seat != X*Y:        # 자리가 다 찰 때까지 반복문
    if G == 1:            # 1번 자리는 이미 차있음
        res = [1, 1]      # 1을 원하면 미리 빼줌
        break
    if G > X*Y:           # G가 전체 다 찬것보다 큰것을 원할 때
        res = [0]         # 0을 출력(마지막에 언패킹 연산자를 써서)
        break

    di,dj = dr[k]         # 방향 좌표 설정
    if 0 <= ti + di < Y and 0 <= tj + dj < X:    # arr를 안넘어가고
        if visited[ti+di][tj+dj] == 0:           # 방문을 하지 않았을 때
            ti = ti + di                         # 위치를 옮겨주고
            tj = tj + dj
            seat += 1                            # 좌석 번호 1 더해줌
            arr[ti][tj] = seat                   # arr에 좌석 번호 입력
            visited[ti][tj] = 1                  # 방문한 곳이라는 것을 체크
            if seat == G:                        # seat이 목표 지점이라면
                res = (ti + 1, tj + 1)           # 인덱스에서 1을 추가해서 좌표로 반환
                break                            # 찾았으니 브레이크

        else:                                    # 방문한 곳이라면 k + 1 ( 방향 전환 )
            k = (k + 1) % 4

    else:                                        # arr를 넘어간다면 k+1 (방향 전환)
        k = (k+1) % 4

print(*res)
