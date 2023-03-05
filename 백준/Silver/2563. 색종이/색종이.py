# Baekjoon 2563번 색종이
'''
가로세로 크기 100인 정사각형 모양의 도화지

이 도화지 위로 가로세로 크기의 각각 10인 검은색 색종이를 붙인다
'''

# import sys
# sys.stdin = open('input.txt', 'r')

arr = [[0]*100 for i in range(100)]
res = 0
N = int(input())
for i in range(N):
    si, sj = map(int,input().split())

    for i in range(10):
        for j in range(10):
            arr[si+i][sj+j] = 1

for i in range(100):
    res += sum(arr[i])

print(res)