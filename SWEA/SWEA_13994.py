# SWEA 13994번 새로운 버스 노선

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):

    cnt = [0]*1001    # 버스 정류소를 1- 1000번까지 인덱스로 쓸것이기 때문에 1001을 곱해주었습니다.
    N = int(input())     # 3

    for _ in range(N):
        Line = list(map(int, input().split()))   # [1, 2, 5]
        if Line[0] == 1:    # 일반 버스
            for i in range(Line[1], Line[2]+1):   # i = [2, 3, 4, 5]
                cnt[i] += 1    # cnt의 i 인덱스위치에 1 더해줌으로 그 정거장에서 몇개의 버스가 지나갔는지 확인

        elif Line[0] == 2:  # 급행 버스    # [2, 3, 10]
            for i in range(Line[1], Line[2] + 1):   # i = [3, 4, ..., 10]
                if Line[1] % 2 == 0:    # 시작점이 짝수
                    if i % 2 == 0:      # 정류소가 짝수일 때 버스가 정차
                        cnt[i] += 1
                elif Line[1] % 2 != 0:  # 시작점이 홀수
                    if i % 2 != 0:      # 정류소가 홀수일 때 정차
                        cnt[i] += 1

        elif Line[0] == 3:   # 광역 버스
            for i in range(Line[1], Line[2] + 1):    # [3, 2, 9]
                if Line[1] % 2 == 0:     # 시작점이 짝수
                    if i % 4 == 0:       # 정류소가 4의 배수일 때 정차
                        cnt[i] += 1
                elif Line[1] % 2 != 0:   # 시작점이 홀수
                    if i % 3 == 0 and i % 10 != 0:    # 정류소가 3의 배수이고 10의 배수가 아닐때 정차
                        cnt[i] += 1

    print(f'#{tc} {max(cnt)}')