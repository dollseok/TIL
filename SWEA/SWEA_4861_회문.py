# SWEA 4861번 회문

'''
ABBA 처럼 어느방향으로 읽어도 같은 문자열을 회문이라함

NxN 크기의 글자판
길이가 M인 회문을 찾아 출력
'''

# 리뷰 : 줄여보기, for 문을 하나로 줄이기

# 짧은 풀이
import sys
sys.stdin = open("input.txt", "r")

def my_len(a):
    cnt = 0
    for _ in list(a):
        cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    res = ''

    arr = list(input() for i in range(N))

    for i in range(N):
        width_list = arr[i]
        length_list = ''.join(arr[j][i] for j in range(N))

        for j in range(N-M+1):
            slice_part_width = width_list[j:j+M]
            if slice_part_width == slice_part_width[::-1]:
                res = slice_part_width
                break

            slice_part_length = length_list[j:j+M]
            if slice_part_length == slice_part_length[::-1]:
                res = slice_part_length
                break

    print(f'#{test_case}', res)


#
# # 긴 풀이
#
# import sys
# sys.stdin = open("input.txt", "r")
#
# # 길이를 확인하는 함수
# def my_len(a):
#     cnt = 0
#     for _ in list(a):
#         cnt += 1
#     return cnt
#
# T = int(input())
# for test_case in range(1,T+1):
#     N, M = map(int, input().split())
#     width_arr = []
#     length_arr = []
#
#     # 가로 arr
#     for i in range(N):
#         width_arr.append(input())
#
#     # 세로 arr 만들기
#     for j in range(N):
#         length_line_list = []
#         for i in range(N):
#             length_line_list.append(width_arr[i][j])
#         length_line = ''.join(length_line_list)
#         length_arr.append(length_line)
#
#
#
#     # 가로 회문 체크
#     for line in width_arr:
#         for k in range(N):
#             for j in range(k+1, N):
#                 if line[k] == line[j]:
#                     slice_part = line[k:j+1]
#                     if slice_part[:] == slice_part[::-1] and my_len(slice_part) == M:
#                         res = slice_part
#
#     # 세로 회문 체크
#     for line in length_arr:
#         for k in range(N):
#             for j in range(k+1, N):
#                 if line[k] == line[j]:
#                     slice_part = line[k:j+1]
#                     if slice_part[:] == slice_part[::-1] and my_len(slice_part) == M:
#                         res = slice_part
#
#     print(f'#{test_case}', res)
