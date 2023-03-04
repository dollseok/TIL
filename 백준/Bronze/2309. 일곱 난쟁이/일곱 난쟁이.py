# Baekjoon 2304번 창고 다각형

'''
아홉 줄에 걸쳐 난쟁이들의 키가 주어진다
키는 100을 넘지 않고 가능한 정답이 여러가지인 경우에는 아무거나 출려간다

부분 집합
'''


# import sys
# sys.stdin = open('input.txt', 'r')

data = [int(input()) for _ in range(9)]
# print(data)    # [20, 7, 23, 19, 10, 15, 25, 8, 13]

n = len(data)    # 9

for i in range(1 << n):    # 000000000 - 111111111 범위 1000000000(이것은 포함 x)
    res = []
    for j in range(n):     # j 9번까지 밀수 있음
        if i & (1 << j):     # 9번 미는데 9자리 중에 1인것만 체크해서 리스트에 추가 
            res.append(data[j])

    if sum(res) == 100 and len(res) == 7:     # 일곱난쟁이, 합이 100
        break

res.sort()
for i in range(7):
    print(res[i])
