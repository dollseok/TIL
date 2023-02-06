# SWEA 4836번 색칠하기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())   # 사각형의 개수
    area1 = []         # 빨간색이 칠해진 영역
    area2 = []         # 파란색이 칠해진 영역
    overlap_list = []  # 겹친 영역

    for _ in range(N):

        x1, y1, x2, y2, c = map(int, input().split())    # 각 끝점의 좌표(x,y)와 컬러색(c)을 받음

        if c == 1:      # 컬러가 빨간색일 때
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    area1.append((i, j))

        elif c == 2:    # 컬러가 파란색일 때
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    area2.append((i, j))

        # print(area1)
        # print(area2)

    for overlap in area1:
        if overlap in area2:
            overlap_list.append(overlap)

        # print(overlap_list)
    print(f'#{test_case} {len(overlap_list)}')