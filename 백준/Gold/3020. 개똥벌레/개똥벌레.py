'''
개똥벌레

1초

동굴 길이 N 200000
높이 H  500000

종유석과 석순이 번갈아가면서 등장 ( 첫번째는 석순(아래서 위로) 짝수는 종유석(위에서 아래))

동굴을 지나가는데 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간의 개수

1. 완전탐색
2중 포문 -> 시간초과

2. 누적합


'''

n,h = map(int,input().split())
arr = [0]
prefix = [0] * (h+1)
for _ in range(n):
    arr.append(int(input()))

for i in range(1,n+1):
    if i % 2 == 0: # 짝수 (종유석)
        prefix[-1] += -1
        prefix[h-arr[i]] += 1
    else: # 홀수 (석순)
        prefix[0] += 1
        prefix[arr[i]] += -1

for i in range(1,h):
    prefix[i] += prefix[i-1]


prefix.pop()
min_ = min(prefix)
print(min_, prefix.count(min_))
