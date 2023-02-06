# SWEA 1945번

# 나의 풀이
import sys
sys.stdin = open("input.txt", "r")

divs = [2, 3, 5, 7, 11]

T = int(input())
for test_case in range(1, T+1):
    cnts = [0] * 5    # 소인수가 5개이므로 개수를 세는 리스트를 인덱스를 5개 가진 리스트로 만듦
    N = int(input())

    for i in range(5):    # div 리스트를 돌리기 위한 범위 설정
        while True:
            if N % divs[i] == 0:    # divs의 값에 대해 나누어진다면
                N = N // divs[i]    # N에는 몫을 넣어주고
                cnts[i] += 1        # cnt 리스트에 divs 인덱스에 1을 더해준다
            else:
                break               # 나누어 지지 않을때는 반복문을 끝냅니다.

    print(f'#{test_case}', *cnts)

# 강의 풀이

# import sys
# sys.stdin = open("input.txt", "r")

# divs = [2, 3, 5, 7, 11]
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     cnts = [0]*len(divs)
#
#     for i in range(len(divs)):
#         while N % divs[i] == 0:
#             cnts[i] += 1
#             N = N // divs[i]
#
#     print(f'#{test_case}', *cnts)


