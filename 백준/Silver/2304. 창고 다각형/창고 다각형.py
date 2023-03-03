# Baekjoon 2304번 창고 다각형

'''
가장 큰 인덱스를 기준으로 앞과 뒤에서 각각 넓이를 더해서 가져옴
'''


# import sys
# sys.stdin = open('input.txt', 'r')


N = int(input())            # 기둥의 개수
data = [list(map(int,input().split())) for _ in range(N)]

# 가장 끝 위치, 가장 높은 위치 파악
mx_L = 0
mx_H = 0
for L, H in data:           # L : 각기둥의 위치 , H : 기둥의 높이
    mx_L = max([mx_L, L])
    mx_H = max([mx_H, H])

# print(mx_L, mx_H)         # 15 10

# [2] 창고 형태 제작
storage = [0]*(mx_L+2)      # 인덱스 에러 안나게 양쪽으로 0 추가해줌
for L, H in data:
    storage[L] = H

# print(storage)              # [0, 0, 4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8, 0]
center = storage.index(mx_H)  # 가장 높은 곳의 위치

area = 0
for i in range(center):                             # 앞에서 뒤로
    area += max([storage[i-1], storage[i]])         # 높이가 더 높은 것을 추가
    storage[i] = max([storage[i-1], storage[i]])    # 높이가 더 높아지면 뒤에 그 앞 위치의 높이를 채워줌
    # print(storage[i], i)
for i in range(mx_L,center-1,-1):                   # 뒤에서 앞으로
    area += max([storage[i], storage[i+1]])         # 높이가 더 높은 것을 추가
    storage[i] = max([storage[i], storage[i+1]])    # 높이가 더 높은게 생기면 더 높은 것을 앞의 위치에 채워줌
    # print(storage[i], i)
#
# print(storage)     # [0, 0, 4, 4, 6, 6, 6, 6, 10, 8, 8, 8, 8, 8, 8, 8, 0]
print(area)
