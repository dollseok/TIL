# 백준 1920번 수 찾기

'''
N개의 정수
리스트
M개의 정수
리스트
'''

N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()

M = int(input())
M_lst = list(map(int,input().split()))

for i in M_lst:
    mx_idx = N - 1
    mn_idx = 0
    middle_idx = (mx_idx + mn_idx) // 2
    if i == N_lst[mx_idx] or i == N_lst[mn_idx] or i == N_lst[middle_idx]:
        print(1)
    elif mx_idx == mn_idx or N_lst[-1] < i:
        print(0)
    else:
        while True:
            if i == N_lst[middle_idx]:
                print(1)
                break
            elif mx_idx == mn_idx or abs(mx_idx-mn_idx) == 1:
                print(0)
                break
            elif N_lst[middle_idx] > i:
                mx_idx = middle_idx
                middle_idx = (mn_idx + mx_idx) // 2
            elif N_lst[middle_idx] < i:
                mn_idx = middle_idx
                middle_idx = (mn_idx + mx_idx) // 2
