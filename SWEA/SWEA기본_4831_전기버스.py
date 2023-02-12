# SWEA 문제 해결 기본 4831번 전기버스
'''
전기버스가 최소한 몇번의 충전소를 거쳐서 끝까지 갈 수 있는지 확인하는 문제
0번에서 N번 정류장까지 이동
한번 충전으로 최대한 이동할 수 있는 정류장 수 = K
충전기가 설치된 M개의 정류장 번호

K, N, M = 3 10 5
충전기 설치된 정류장 번호 = 1 3 5 7 9

'''


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K = 한번 충전으로 이동하는 정류장 수
    # N = 전체 정류장 수
    # M = 충전기가 설치된 정류장 번호

    charge_station = list(map(int, input().split()))     # 충전기가 있는 정류소 리스트

    station = list(range(N+1))    # 전체 정류장의 리스트

    max_D = K       # 한번의 충전으로 최대 갈 수 있는 거리를 K 값으로 설정, 1씩 줄여가면서 최대 거리 안에 충전기가 있는지 확인할 예정
    i = 0           # 버스가 출발하는 기준점
    charge_cnt = 0  # 충전 횟 수 

    while True:

        if i >= N - max_D:    # 마지막 충전기로부터 끝까지 갈 수 있으면 충전기가 이제 필요 없으므로 break
            break

        # elif부분을 먼저 설명하고 if 문을 설명하는게 매끄러움
        if station[i+max_D] in charge_station:    # 충전한 것으로 갈 수 있는 최대 거리에 충전기가 있으면
            charge_cnt += 1        # oil cnt를 하나 추가
            i = i + max_D       # max_D를 더한 위치까지 보냄
            max_D = K           # max_D값 초기화
            # continue

        elif station[i+max_D] not in charge_station:    # 최대치로 갈수 있는 장소에 충전기가 없으면
            max_D = max_D-1     # 1만큼 더 가까운 곳에 있는지 확인하기 위해 max_D를 줄임
            if max_D == 0:      # max_D가 0이면 최대로 가는 곳에 충전기가 없으므로
                charge_cnt = 0     # 끝까지 못가므로 oil cnt를 0으로 넣고 마무리
                break

    print(f'#{tc} {charge_cnt}')
