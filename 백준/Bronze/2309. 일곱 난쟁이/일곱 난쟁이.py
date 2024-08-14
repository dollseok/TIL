'''
일곱난장이 키 합이 100이다
가능한 답이 여러개면 아무거나 출력

7이여야하는데 9가 들어옴
9개 중에 7개 선택 => 총 100개 안됨

1. combi로 풀어라
2. 완탐 방식은 어떤 것일까?

'''

from itertools import combinations

lst = []
for _ in range(9):
    lst.append(int(input()))

for comb in combinations(lst,7):
    if sum(comb) == 100:
        comb = sorted(list(comb))
        for i in comb:
            print(i)
        break



# def combi(arr,r):
#     result = []
#     if r > len(arr):
#         return result
#
#     if r == 1:
#         for i in arr:
#             result.append([i])
#     elif r > 1:
#         for i in range(len(arr) - r + 1 ):
#             for j in combi(arr[i+1:],r-1):
#                 result.append([arr[i]]+j)
#
#     return result
#


