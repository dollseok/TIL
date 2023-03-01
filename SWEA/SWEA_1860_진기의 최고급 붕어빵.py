#SWEA 1860번 진기의 최고급 붕어빵

'''
조건들에 유의해야하는 문제
붕어빵은 0초부터 만들긴하지만 첫 붕어빵이 나오는 것은 다음 시간 부터
사람은 오픈 시간 0초부터 올수도 있다.
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())                  # N : 사람수, M : 만드는데 걸리는 시간, K개 붕어빵 제작
    person_time = list(map(int, input().split()))        # N개 만큼 있다.

    bread_timeline = [0]*(max(person_time)+1)            # 빵이 구워지는 타임 라인, 인덱스 사용할 것

    res = 'Possible'

    for i in range(len(bread_timeline)):
        bread_timeline[i] += bread_timeline[i-1]         # 앞시간에 붕어빵이 안팔리고 남아있으면 뒤에 추가

        if i % M == 0 and i != 0:                        # M 시간 마다 붕어빵이 나옴 0초일때 제외
            bread_timeline[i] += K                       # K 개 만큼 추가

        if i in person_time:                             # 손님이 온 시간이면
            bread_timeline[i] -= person_time.count(i)    # 한타임에 여러명 올수 있으니 그 인원 수만큼 빼준다
            if bread_timeline[i] <= -1:                  # -1보다 작아지면 바로 나눠주지 못한 것
                res = 'Impossible'                       # 결과 impossible 받고 브레이크
                break

    print(f'#{test_case}', res)

