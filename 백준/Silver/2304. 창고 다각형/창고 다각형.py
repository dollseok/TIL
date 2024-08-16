'''
창고 다각형

오목한 부분이 없게 -> 양끝에서부터 계속 높은 형태로

1. 가장 높은 것 기준까지 양끝에서 가운데로 모은다
2. 기준점의 앞뒤로 점화식 형식


'''


N = int(input())
dict = {}
max_h = 0
start = 0
end = 1001
for _ in range(N):
    L, H = map(int,input().split())
    max_h = max(max_h,H)
    start = min(start,L)
    end = max(end,L)
    dict[L] = H

current = 0
result = 0
comeback_idx = 0

for i in range(start,end+1):
    if i in dict.keys() and current < dict[i]:
        current = dict[i]
    result += current

    # 중간 최고값 도착
    if current == max_h:
        comeback_idx = i
        break

# 가장 뒤에서 앞으로
current = 0
for j in range(end, comeback_idx,-1):
    if j in dict.keys() and current < dict[j]:
        current = dict[j]
    result += current

print(result)




