# 백준 2609번 최대공약수와 최소공배수

'''
최대 공약수, 최소 공배수
'''

# import sys
# sys.stdin = open('input.txt', 'r')

N,M = map(int, input().split())

if N > M:
    startnum = M
    othernum = N
else:
    startnum = N
    othernum = M



# if N != 1 and M != 1:
for i in range(startnum,0,-1):
    if N % i == 0:
        if M % i == 0:
            res1 = i
            break

print(res1)

for i in range(1,startnum+1):
    if othernum*i % startnum == 0:
        res2 = othernum*i
        break
print(res2)

# elif N == 1:
#     print(1)
#     print(M)
#
# elif M == 1:
#     print(1)
#     print(N)