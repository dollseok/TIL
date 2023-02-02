# SWEA 4831번 전기버스
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    K,N,M = map(int, input().split())
    M_list = list(map(int, input().split()))     # 입력값을 받음

    N_list = list(range(N+1))    # 전체 정류장의 list를 만들어줌

    max_D = K    # 최대 갈 수 있는 거리를 K값으로 1차적으로 고정해줌
    i = 0
    oil_cnt = 0

    while True:

        if i >= N - max_D:    # 마지막 충전기로부터 끝까지 갈 수 있으면 충전기가 이제 필요 없으므로 break
            break

        if N_list[i+max_D] in M_list:    # 충전한 것으로 갈 수 있는 최대 거리에 충전기가 있으면
            oil_cnt += 1        # oil cnt를 하나 추가
            i = i + max_D       # max_D를 더한 위치까지 보냄
            max_D = K           # max_D값 초기화
            continue

        elif N_list[i+max_D] not in M_list:    # 최대치로 갈수 있는 장소에 충전기가 없으면
            max_D = max_D-1     # 1만큼 더 가까운 곳에 있는지 확인하기 위해 max_D를 줄임
            if max_D == 0:      # max_D가 0이면 최대로 가는 곳에 충전기가 없으므로
                oil_cnt = 0     # 끝까지 못가므로 oil cnt를 0으로 넣고 마무리
                break

    print(f'#{tc} {oil_cnt}')
