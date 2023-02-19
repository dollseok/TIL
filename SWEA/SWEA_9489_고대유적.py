#SWEA 9489번 고대 유적

'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYXI5IoKVCoDFAQK&contestProbId=AXAd8-d6MRoDFARP&probBoxId=AYYK3r76yQwDFARc&type=USER&problemBoxTitle=%EC%97%B0%EC%8A%B5%28%EC%B6%94%EC%B2%9C%EB%AC%B8%EC%A0%9C%29&problemBoxCnt=19

접근 방법

1. 전체리스트에 패딩을 추가한다
2. 1을 만났을 때 좌우로 1이 또 있다면 그 방향에서 가장 끝으로 가서 반대쪽 끝으로 가면서 그 줄의 길이를 잰다
3. 1을 만났을 때 상하로 1이 있다면 그 방향에서 가장 끝으로 가서 그 반대쪽 끝으로 가면서 그 줄의 길이를 잰다
4. 최대로 긴 것을 미리 뽑아낸다
5. 모든 1에 대해서 같은 처리를 한다.
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for Test_case in range(1, T+1):
    cnt = 0
    N, M = map(int, input().split())    # N = 세로(줄 수) M = 가로 줄당 개수

    ground = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]  # 상하좌우 패딩 추가된 유적지
    ground = [[0] * (M+2)] + ground + [[0] * (M+2)]
    max_length = 0

    for i in range(1, N+1):
        for j in range(1, M+1):
            if ground[i][j] == 1:

                if ground[i+1][j] == 1 or ground[i-1][j] == 1:        # 좌우로 1이 있을 때
                    ti = i                                            # 임시 좌표 설정
                    tj = j
                    length = 0                                        # 길이 늘 0으로 초기화
                    while ground[ti][tj] != 0:                        # 0이 아닐 동안 (0을 만날 때까지)
                        ti -= 1                                       # 가장 왼쪽 끝으로 간다
                    ti += 1                                           # 0의 위치 바로 오른쪽 한칸 이동

                    while ground[ti][tj] != 0:                        # 0이 아닐 동안
                        ti += 1                                       # 가장 오른쪽 끝으로 간다
                        length += 1                                   # 가는 동안 길이 하나씩 추가
                    if max_length < length:                           # 최대 길이인지 확인
                        max_length = length

                if ground[i][j+1] == 1 or ground[i][j - 1] == 1:      # 위아래로 1이 있을 때, 위의 과정 반복
                    ti = i
                    tj = j
                    length = 0
                    while ground[ti][tj] != 0:
                        tj -= 1
                    tj += 1

                    while ground[ti][tj] != 0:
                        tj += 1
                        length += 1

                    if max_length < length:
                        max_length = length

    print(f'#{Test_case} {max_length}')

