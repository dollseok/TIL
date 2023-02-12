#SWEA 2001번 파리 퇴치

'''
NxN 배열 안의 숫자는 파리의 개수
MxM 배열의 파리채를 한번 내리쳐서 가장 많이 파리를 죽였을 때, 죽인 파리 개수 구하기
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N : 영역의 넓이 , M : 파리채 사이즈

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt_flys = 0

    for i in range(N-M+1):
        for j in range(N-M+1):     # 기준점이 N-M 인덱스까지임
            cnt_flys = 0           # 인덱스마다 0으로 리셋
            for k in range(M):     # 기준점으로부터 파리채의 범위
                for a in range(M):   # 같은 범위인데 왜 굳이 두번을 돌았지? 삭제 # 했는데 틀림 - 왜냐면 가로 세로 두번씩 돌아야하기때문
                    cnt_flys += arr[i+k][j+a]

            if max_cnt_flys < cnt_flys:
                max_cnt_flys = cnt_flys

    print(f'#{test_case} {max_cnt_flys}')

