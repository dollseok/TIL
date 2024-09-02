'''
연속된 k개의 신호등이 존재하려면?
N개의 횡단 보도
연속된 K개의 신호등이 존재하게 수리
B개의 줄에 고장난 신호등
'''

n,k,b = map(int,input().split())

ls = [1]*n

for _ in range(b):
    ls[int(input())-1] = 0 # 고장 표시

i = 0
j = 0
fix_cnt = 0
if ls[0] == 0:
    fix_cnt = 1
length = 1
result = 100001
# print(ls)
while j < n:
    if length == k:
        result = min(result,fix_cnt)
        length += 1
        j += 1
        if j != n and ls[j] == 0:
            fix_cnt += 1
    elif length > k:
        length -= 1
        if ls[i] == 0:
            fix_cnt -= 1
        i += 1
    else:
        length += 1
        j += 1
        if ls[j] == 0:
            fix_cnt += 1

    # print(i, j, length, fix_cnt)

if result == 100001:
    print(0)
else:
    print(result)