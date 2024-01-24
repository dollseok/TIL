'''
최대한 빠른 마을에서 최대한 내려주고 다 싣는게 좋다

Point
- 내려주는게 빠를 수록 좋다는 것
- 그 사이에 얼마나 많은 짐이 이미 있는지 확인하는 것
- 최대로 옮겨서 가져갈수 있는게 얼마인지 그 위치까지, 그리고 그 모든 위치에서 최대 용량을 안넘는지 확인
'''

n,c = map(int,input().split())
m = int(input()) # 배달 데이터 개수

data = [list(map(int,input().split())) for _ in range(m)]

sort_data = sorted(data, key=lambda x: (x[1]))
village = [0]*(n+1) # 각 지역별 옮길수 있는 최대 개수

result = 0

for start,end,amount in sort_data:
    temp = amount
    for i in range(start,end):
        if village[i] +temp >= c:
            temp = c-village[i]
    for i in range(start,end):
        village[i] += temp
    result += temp
    # print(village)

print(result)
