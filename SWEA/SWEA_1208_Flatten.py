# SWEA 1208번 Flatten


'''
높은 곳의 상자를 낮은 곳에 옮기는 문제
최고점의 상자를 가장 낮은 곳을 옮긴다

그리고 최고점과 최저점의 차이를 구한다.

hint
시뮬레이션 해보는 것
상자의 높이가 100x100


나는 sort를 생각했다.

'''

import sys
sys.stdin = open("input.txt", "r")

# 강의 풀이

# def get_max_idx():
#     max_value = 0
#     max_idx = -1   # 초기값은 유효하지않은 값으로 설정
#
#     for i in range(len(boxes)):
#         if boxes[i] > max_value:
#             max_value = boxes[i]
#             max_idx = i
#
#     return max_idx
#
# def get_min_idx():
#     min_value = 99999999999      # 초기값은 영향을 주지않는 최소값
#     min_idx = -1
#
#     for i in range(len(boxes)):
#         if boxes[i] < min_value:
#             min_value = boxes[i]
#             min_idx = i
#
#     return min_idx
#
# for test_case in range(1,11):
#     n = int(input())
#     boxes = list(map(int, input().split()))
#
#     for i in range(n):   # 덤프 횟수 제한
#         boxes[get_max_idx()] -= 1
#         boxes[get_min_idx()] += 1
#
#     res = boxes[get_max_idx()] - boxes[get_min_idx()]
#     print(f'#{test_case} {res}')


# 내 풀이 함수사용

# for test_case in range(1,11):
#     n = int(input())
#     boxes_list = list(map(int, input().split()))
#     boxes_list.sort()
#     # print(boxes_list)
#     for i in range(n):   # n번만큼 덤프를 한다.
#         boxes_list[-1] -= 1
#         boxes_list[0] += 1
#         boxes_list.sort()
#
#     print(boxes_list[-1] - boxes_list[0])
