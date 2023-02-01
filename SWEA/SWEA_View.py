# SWEA view
'''
문제 링크

https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYXI5IoKVCoDFAQK&contestProbId=AV134DPqAA8CFAYh&probBoxId=AYXI6OVKVLsDFAQK&type=PROBLEM&problemBoxTitle=%EA%B3%BC%EC%A0%9C&problemBoxCnt=3

양 옆으로 2칸이 비어있는 층의 집이 조망권이 좋은 집
조망권이 좋은 집의 개수를 구하는 것이 문제 목표

'''


# import sys
# sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))   # 입력값을 받는 줄

    room_cnt = 0    # 조망권이 좋은 집 개수 = 0

    for i in range(2, N-2):    # 양 끝에 0이 두집씩 있다.
        side_list = [lst[i-2], lst[i-1], lst[i+1], lst[i+2]]    
        # i 기준부터 양쪽 두집씩 층들을 리스트로 꺼냄
        max_side = 0    # 양쪽 두집들 중 최대값을 변수 설정

        for j in side_list:    
            if j >= max_side:
                max_side = j     
            # max를 알고리즘으로 표현, max_side의 값(최대값)을 side_list에서 꺼냄

        if lst[i] > max_side:
            room_cnt += (lst[i] - max_side)
        # 기준값이 max_side보다 크면 그 정도의 집 개수만큼 추가해준다

    print(f'#{tc} {room_cnt}')