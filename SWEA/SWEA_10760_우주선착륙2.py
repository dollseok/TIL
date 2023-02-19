#SWEA 10760번 우주선착륙2

import sys
sys.stdin = open("input.txt", "r")

di = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

T = int(input())
for test_case in range(1,T+1):
    N, M = map(int, input().split())

    # 패딩 추가한 arr 제작
    # 높이 최대가 9이므로 더 높은 10으로 겉을 감싸줌
    main_arr = [[10]+list(map(int, input().split())) + [10] for _ in range(N)]
    arr = ([[10]*(M+2)] + main_arr + [[10]*(M+2)])



    res = 0        # 후보지 개수
    for i in range(1, N+1):
        for j in range(1, M+1):
            cnt = 0
            for k in range(8):      # 8방향 확인

                if arr[i + di[k][0]][j + di[k][1]] < arr[i][j]:    # 이동한 위치가 지금보다 낮으면
                    cnt += 1                                       # 개수를 세준다

                if cnt == 4:         # 4개 이상이라는 조건이 되면
                    res += 1         # 이미 후보지임으로 res 추가하고 for 문 break
                    break

    print(f'#{test_case} {res}')
