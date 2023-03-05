# Baekjoon 2559번 수열

'''
측정한 온도가 어떤 정수의 수열로 주어졌다
연속적인 며칠 동안 온도합이 가장 큰 값?

'''

# import sys
# sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
data = list(map(int, input().split()))

res = sum([data[i] for i in range(K)])
sum_K = sum([data[i] for i in range(K)])

for i in range(K, N):
    sum_K = sum_K - data[i-K] + data[i]
    res = max([sum_K, res])

print(res)