# 백준 2108번 통계학

'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값  : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값  : N개의 수들 중 가장 많이 나타나는 ㄱ밧
범위    : N개의 수들 중 최대 값과 최소 값의 차이
'''

# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())

data = [int(input()) for i in range(N)]

# print(data)

# 산술 평균
print(round(sum(data)/N))

# 중앙 값
data.sort()
print(data[N//2])

# 최빈값

res_dict = {}

for i in data:
    if res_dict.get(i):
        res_dict[i] = res_dict[i] + 1
    else:
        res_dict[i] = 1

val_dict = list(res_dict.values())
key_dict = list(res_dict.keys())
mx = max(val_dict)
len_ = len(val_dict)
res_list = []
for i in range(len_):
    if val_dict[i] == mx:
        res_list.append(key_dict[i])
        res = res_list[0]

    if len(res_list) == 2:
        res = res_list[1]
        break


print(res)

# 4. 범위
print(max(data)-min(data))



