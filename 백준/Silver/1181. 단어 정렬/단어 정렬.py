import sys
input = sys.stdin.readline


T = int(input())

w_list = [input().strip() for _ in range(T)]

w_dict = {}
for i in w_list:
    w_dict[i] = len(i)

new_list = list(zip(w_dict.keys(), w_dict.values()))

new_list.sort(key = lambda x: x[0])
new_list.sort(key = lambda x: x[1])

for i in new_list:
    print(i[0])
