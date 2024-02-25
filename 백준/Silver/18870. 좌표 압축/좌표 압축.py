'''
18870번 좌표 압축
'''

n = int(input())
data = list(map(int,input().split()))

set_ = sorted(list(set(data)))
dict = {}

for i in range(len(set_)):
    dict[set_[i]] = i

for i in range(n):
    data[i] = dict[data[i]]

print(*data)