# 백준 2578번 빙고

'''
1-5줄 빙고 arr
6-10줄 사회자가 읽는 숫자 리스트
'''

# import sys
# sys.stdin = open('input.txt','r')

arr = [list(map(int, input().split())) for _ in range(5)]
arr_t = list(map(list, zip(*arr)))
diag1 = []
diag2 = []
read_list = []
for i in range(5):
    read_list += list(map(int, input().split()))

for i in range(5):
    diag1.append(arr[i][i])
    diag2.append(arr[i][4-i])

# data 각 줄들이 모두 0이 되면 빙고 [0,0,0,0,0]
data = arr + arr_t + [diag1] + [diag2]

while True:
    for read in read_list:
        for i in range(12):
            for j in range(5):
                if data[i][j] == read:
                    data[i][j] = 0

        bingo = data.count([0, 0, 0, 0, 0])

        if bingo >= 3:
            res = read_list.index(read)
            break

    if bingo >= 3:
        break

print(res+1)