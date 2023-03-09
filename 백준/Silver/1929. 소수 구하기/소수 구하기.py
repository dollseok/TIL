# 백준 1929번 소수 구하기

'''
M 이상 N이하의 소수를 모두 출력하는 프로그램
에라토스테네스의 체
'''

# import sys
# sys.stdin = open('input.txt', 'r')

M, N = map(int,input().split())
res = [1] * (N+1)

for i in range(2, N+1):
    for j in range(2, N+1):
        if i*j > N:
            break
        res[i*j] = 0

for i in range(M,N+1):
    if res[i] and i != 1:
        print(i)


# 에라토스테네스의 수

# M, N = map(int, input().split())
# res = [1]*(N+1)    # 인덱스 활용
# K = int(N**0.5)    # 그보다 작은 제곱수까지의 소수까지만 확인
#
# for i in range(2,K+1):
#     if res[i]:
#         for j in range(i+i, N+1, i):    # 소수 i의 배수들 확인
#             res[j] = 0
#
# for i in range(M, N+1):
#     if res[i] and i != 1:
#         print(i)



# # 시간 초과 풀이
# M, N = map(int,input().split())
# res = []
#
# for i in range(1,N+1):
#     cnt = 0
#     for j in res:
#         if i % j == 0 and j != 1:
#             cnt += 1
#             break
#     if cnt == 0:
#         res.append(i)
#         k = res[-1]
#         if k >= M:
#             print(k)

