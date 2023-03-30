# SWEA 10816번 숫자 카드2

'''
숫자 카드 N개, 주어지는 정수 M개
이 수가 적혀있는 숫자 카드를 상근이가 몇개 가지고 있나?
'''

# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
N_data = list(map(int,input().split()))
N_set = set(N_data)
M = int(input())
M_data = list(map(int, input().split()))
res_list = [0]*M
dict = {}

# for 안에 count라 시간복잡도가 M*N으로 제곱이 나와서 시간 초과
# for i in range(M):
#     a = M_data[i]
#     if a in N_set:
#         res_list[i] = N_data.count(a)

for i in M_data:
    dict[i] = 0

for i in range(N):
    if dict.get(N_data[i],'Nothing') != 'Nothing':
        dict[N_data[i]] = dict[N_data[i]] + 1

for i in M_data:                # M 데이터가 중복으로 들어오는 경우 해결
    print(dict[i], end=' ')