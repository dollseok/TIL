# SWEA 문제 해결 기본 4881번 배열 최소합

'''
한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록하려고한다.
단 세로로 같은 줄에서 두개 이상의 숫자를 고를 수 없다.

조건에 맞게 숫자를 골랐을 때 최소 합을 출력하는 프로그램
'''

import sys
sys.stdin = open("input.txt", "r")

def backtracking(i,target,s):        # (시작지점, target 지점, 총합)
    global minS                      # 외부에서 minS를 가져옴
    if i == target:                  # i 가 타겟점에 도착했을 때
        # print(s)
        if s < minS:                 # 총합이 minS보다 작으면
            minS = s                 # 최소값을 새로 설정
    elif s > minS:                   # s가 이미 minS보다 크면 의미 없으므로 함수 마무리
        return

    else:
        for j in range(N):           # N개를 새로로 볼것
            if not visited[j]:       # 그 줄에 이미 들렸던 장소가 없으면
                visited[j] = True    # True를 넣는다 (이미 나왔던 장소임을 보여줌)
                backtracking(i+1, target, s+arr[i][j])  # 다음 i를 확인하면서, 총합에 arr[a][j] 값을 추가
                visited[j] = False

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]      # 주어진 input의 arr을 받음
    visited = [False] * N                                          # 세로에 대해서 겹치면 안됨으로 지나간 길은 True 처리 예정
    # print(arr)
    minS = 9999         # 최소값을 큰 값으로 잡아둠

    backtracking(0,N,0)     # (시작지점, target 지점, 총합)

    print(f'#{test_case}', minS)

