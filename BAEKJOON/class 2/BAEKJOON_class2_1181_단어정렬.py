# BAEKJOON class2 1181번 단어 정렬

'''
https://www.acmicpc.net/problem/1181
1. 길이가 짧은 것 부터
2. 길이가 같으면 사전 순으로
'''

import sys
sys.stdin = open('input.txt','r')

import sys
input = sys.stdin.readline
# 이 문제에서 사용하면 출력형식 오류, 이유 : 개행 문자 \n까지 가져와서 strip 으로 지워줘야 함


T = int(input())

w_list = [input().strip() for _ in range(T)]

w_dict = {}
for i in w_list:
    w_dict[i] = len(i)                                   # key에 단어, value에 길이인 딕셔너리

new_list = list(zip(w_dict.keys(), w_dict.values()))     # 딕셔너리에서 튜플형식으로 각각에 묶어줌

new_list.sort(key = lambda x: x[0])                      # 단어에 대한 정렬
new_list.sort(key = lambda x: x[1])                      # 길이에 대한 정렬
# print(new_list)

for i in new_list:
    print(i[0])















# 시간 초과 난 풀이

#
# T = int(input())
#
# first_w_list = [input() for _ in range(T)]
#
#
# w_list = []
#
# for i in range(T):
#     if first_w_list[i] not in w_list:
#         w_list.append(first_w_list[i])
#
# l = len(w_list)
#
# for i in range(l-1):
#     for j in range(i+1,l):
#
#         if len(w_list[i]) > len(w_list[j]):
#             w_list[i],w_list[j] = w_list[j], w_list[i]
#
#         elif len(w_list[i]) == len(w_list[j]):
#             for k in range(len(w_list[i])):
#                 if w_list[i][k] > w_list[j][k]:
#                     w_list[i], w_list[j] = w_list[j], w_list[i]
#                     break
#                 elif w_list[i][k] < w_list[j][k]:
#                     break
#                 else:
#                     continue
#
# for i in w_list:
#     print(i)
