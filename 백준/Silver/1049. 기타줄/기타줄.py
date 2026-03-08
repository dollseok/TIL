'''

N개의 줄이 필요

'''
N,M = map(int,input().split())

set_count = N // 6
set_list = []
individual_list = []

for _ in range(M):
    s, i = map(int, input().split())
    set_list.append(s)
    individual_list.append(i)


res = 9999999999999999999
for i in range(set_count + 2):
    individual_count = N - i * 6
    if individual_count < 0:
        individual_count = 0
    res = min(res, i * min(set_list) + individual_count * min(individual_list))


print(res)