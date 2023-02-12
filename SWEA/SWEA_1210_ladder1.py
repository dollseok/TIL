#SWEA 1210번 Ladder1

'''
사다리 타기하는 문제
도착 지점이 2인 곳을 찾는 것
시작지점을 출력

풀이
도착지점에서 시작하면 쉽다

'''


import sys
sys.stdin = open("input.txt", "r")

for i in range(10):
    Test_case = int(input())
    # 양쪽에 패딩 [0]을 추가해서 arr을 만든다
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    start_i = 99                        # 가장 아래 지점
    start_j = arr[start_i].index(2)     # 원하는 도착지점 = 2 인 인덱스를 찾아서 j의 시작 지점

    while start_i != 0:                           # 위로 올라간다
        if arr[start_i][start_j - 1] == 1:        # 왼쪽이 1일 때
            while arr[start_i][start_j-1] != 0:   # 0이 되기 전까지 (사다리의 끝)
                start_j -= 1                      # 사다리의 끝까지 간다
            start_i -= 1                          # 끝에서 바로 한칸 올라감
        elif arr[start_i][start_j + 1] == 1:      # 오른쪽이 1일 때
            while arr[start_i][start_j + 1] != 0:
                start_j += 1
            start_i -= 1
        else :
           start_i -= 1                            # 양쪽이 다 1이 아니면 위로 계속 올라감

    print(f'#{Test_case} {start_j-1}')


