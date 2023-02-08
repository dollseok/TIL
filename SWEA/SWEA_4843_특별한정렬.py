# SWEA 4843번 특별한 정렬

'''
N개의 정수가 주어지면 가장 큰 수, 가장 작은수, 2번째 큰수, 2번째 작은수 식으로 큰수와
작은 수를 번갈아 정렬

주어진 숫자의 결과를 10개까지만 출력
'''

import sys
sys.stdin = open("input.txt", "r")


def selection_small(list, k):    # k번째로 작은 수
    for i in range(k):
        minIdx = i
        for j in range(i + 1, len(list)):
            if list[minIdx] > list[j]:
                minIdx = j
        list[i], list[minIdx] = list[minIdx], list[i]

    return list[k-1]


def selection_big(list, k):      # k번째로 큰 수
    for i in range(k):
        maxIdx = i
        for j in range(i+1, len(list)):
            if list[maxIdx] < list[j]:
                maxIdx = j
        list[i], list[maxIdx] = list[maxIdx], list[i]

    return list[k-1]


T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr_list = []

    for i in range(1, N//2 + 1):
        new_arr_list.append(selection_big(arr, i))
        new_arr_list.append(selection_small(arr, i))

    print(f'#{test_case}', *new_arr_list[:10])


