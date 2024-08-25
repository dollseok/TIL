'''

수들의 합

2 -2 2 -2

i,j 0으로 시작
K 보다 현재 값이 작거나 같으면 늘려주는 방향
'''

from collections import deque

q = deque()

N,K = map(int,input().split())
arr = [0] + list(map(int,input().split()))
prefix = [0]*(N+1)
dict_ = {0:1}

for i in range(1,N+1):
    prefix[i] = prefix[i-1] + arr[i]

answer = 0
for i in range(1,N+1):
    current = prefix[i]
    if current - K in dict_.keys():
        answer += dict_[current-K]

    if current in dict_.keys():
        dict_[current] += 1
    else:
        dict_[current] = 1

print(answer)

