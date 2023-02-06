# baekjoon 5585번 거스름돈

'''
500엔, 100엔, 50엔, 10엔, 5엔, 1엔의 거스름돈
'''

import sys
sys.stdin = open("input.txt", "r")


money = 1000 - int(input())

change = [500, 100, 50, 10, 5, 1]
change_cnt = [0]*6

for i in range(6):
    if money >= change[i]:
        change_cnt[i] = money // change[i]
        money = money % change[i]

# print(change_cnt)
print(sum(change_cnt))