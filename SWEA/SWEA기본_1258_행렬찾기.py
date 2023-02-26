#SWEA 문제 해결 응용 1258번 행렬찾기

'''
개수, 사이즈: 가로j 세로i 순서로 출력, 작은 순서로 출력

전체를 돌다가 기준점을 발견하면
dr로 가로와 세로 구해서 결과리스트에 리스트 혹은 튜플로 넣기
두 원소 곱한값이 작은 순서로 정렬하고 카운트

개수, 가로세로 순으로 출력

왜 틀릴까..?
마지막 조건 확인을 안했다
" 크기가 같을 경우 행이 작은 순으로 출력한다."
'''

import sys
sys.stdin = open("input.txt", "r")

def boundary(i,j):
    si = i    # 시작점(왼쪽 아래) 저장해둔다
    sj = j

    global res_list

    while arr[i][j] != 0: # 오른쪽 방향이 0이 나올때까지 간다.
        j = j + 1
    bound_j = j - 1       # 0을 만나면 다시 0 만나기 직전으로 돌린다

    while arr[i][bound_j] != 0:
        i = i + 1
    bound_i = i - 1

    # 방문한 곳 한번에 처리 (시작점 - 경계선까지)
    for i in range(si, bound_i + 1):
        for j in range(sj, bound_j + 1):
            visited[i][j] = 1

    res_list.append([bound_i - si + 1, bound_j - sj + 1])  # 길이는 경계값 빼주고 +1 해주는 것

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    # 패딩 붙여준다
    arr = [[0] + list(map(int,input().split())) + [0] for _ in range(N)]
    arr = [[0]*(N+2)]+ arr + [[0]*(N+2)]
    visited = [[0]*(N+2) for _ in range(N+2)]
    res_list = []

    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] != 0 and visited[i][j] == 0:      # 시작점을 만났으면 함수 시작
                boundary(i, j)

    res_list.sort(key = lambda x : x[0])          # 크기가 같을 경우 행이 작은 순으로 출력한다.
    res_list.sort(key = lambda x : (x[0]*x[1]))   # 크기가 작은 것 부터 정렬

    print(f'#{test_case} {len(res_list)}', end = ' ')
    for l in res_list:
        print(*l, end=' ')
    print()


