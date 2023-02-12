# SWEA 1221번 GNS

'''
문자로 되어있는 0-9 리스트를 정렬하는 문제

처음엔 인덱스 오류로 인해 마지막 것을 정렬하지 못했었다.
'''


import sys
sys.stdin = open("input.txt", "r")

# 간단한 풀이
#
# T = int(input())
# for test_case in range(T):
#     tc, N = input().split()
#     line = list(input().split())     # 나누어서 각 원소로 line이라는 리스트에 받음
#     num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     res = []
#
#     for i in num:                   # num에 있는 각 원소에 대하여
#         for j in range(int(N)):     # line의 길이(N)에 따라
#             if i == line[j]:        # 같으면
#                 res.append(i)       # i를 res에 추가해줌
#
#     print(f'{tc}')
#     print(*res)

#진짜 딕셔너리를 이용한 풀이

T = int(input())
for test_case in range(T):
    GNS_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    res = ''
    tc, N = input().split()
    line = list(input().split())

    for i in line:
        GNS_dict[i] += 1

    for i in GNS_dict.keys():
        res += (i + ' ')*GNS_dict[i]     # 이어서 한칸 공백과 추가를 하기 때문에 ' ' 를 붙여서 더해줌

    print(f'{tc}')
    print(res)
    # print(res.rstrip())   # 옆에 공백 빼줘야하는 줄 알았는데 없어도 오류 없이 패스



# 안되는 코드 왜지..?

# 마지막에 보면 한 단어가정리가 안되어있음, 확인하기

# GNS_dict = {}          # 문자를 숫자로 만들 딕셔너리
# GNS_dict_rev = {}      # 숫자를 문자로 다시 만들 딕셔너리
#
# key = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for o in range(10):
#     GNS_dict[key[o]] = value[o]        # key와 value가 서로 반대인 딕셔너리를 만들어줌
#     GNS_dict_rev[value[o]] = key[o]
#
# T = int(input())
# for test_case in range(T):
#     tc, N = input().split()
#     line = list(input().split())
#
#     for k in range(int(N)):
#         line[k] = GNS_dict[line[k]]          # 문자로 된 숫자를 진짜 숫자로 만들어줌
#
#     for i in range(int(N)-1):                # 오름차순으로 버블 정렬
#         for j in range(i+1, int(N)):
#             if line[i] > line[j]:
#                 line[i], line[j] = line[j], line[i]
#
#     for t in range(int(N)):                  # 숫자를 다시 문자로 만들어줌
#         line[t] = GNS_dict_rev[line[t]]
#
#     print(f'{tc}')
#     print(*line)
#




