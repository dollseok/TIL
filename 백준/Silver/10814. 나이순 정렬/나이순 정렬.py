# SWEA 10814번 나이순 정렬

'''
나이 이름이 가입한 순서대로 주어진다.
'''

# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())    # N = 회원 수
lst = [[]]*201
age_lst = []
# print(lst)

for i in range(N):
    age, name = input().split()
    lst[int(age)] = lst[int(age)] + [name]

for i in range(201):
    if lst[i]:
        for j in lst[i]:
            print(f'{i} {j}')


