'''
빗물
1초
고이는 빗물의 총량
비가 오면 블록 사이에 빗물 고임

세로길이 H, 가로길이 W 둘다 최대 500

1. 완전탐색
최고점을 찾고 그 기준으로 앞에서 올라오고 뒤에서 내려오고

'''


H,W = map(int,input().split())
arr = [0] + list(map(int,input().split()))
prefix = [0]*(W+1)

max_idx = arr.index(max(arr))
current = 0

for i in range(1,max_idx):
    if arr[i] < current:
        prefix[i] += current - arr[i]
    else:
        current = arr[i]


current = 0
for j in range(W,max_idx,-1):
    if arr[j] < current:
        prefix[j] += current - arr[j]
    else:
        current = arr[j]

print(sum(prefix))