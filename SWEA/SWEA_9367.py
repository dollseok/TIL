# SWEA 9367 점점 커지는 당근의 개수

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())     # N = 5   당근의 개수
    C_list = list(map(int, input().split()))    # 수확한 순서로 받은 당근의 크기
    cnt = 1     # 기본적으로 최소가 1
    cnt_max = 1 # 가장 작더라도 1 그래서 변수 설정을 기본 1로 해줌
    for i in range(N-1):    # 제일 끝에 것은 뒤에 비교할 것이 없기때문에 N-1까지 범위 설정
        if C_list[i] + 1 == C_list[i+1]:    # i번째 당근에 1을 더해줫을 때 뒤에 것과 같으면 연속
            cnt += 1    # cnt를 추가해주면서 연속이 얼마나 되는지 확인
            if cnt > cnt_max:    # cnt가 최대값이라면 cnt_max에 할당
                cnt_max = cnt
        else:    # 연속이 되지 않았을 때
            cnt = 1    # cnt를 1로 리셋 시켜줍니다.

    print(f'#{tc} {cnt_max}')