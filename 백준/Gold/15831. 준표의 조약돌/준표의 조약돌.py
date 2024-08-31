'''
조약돌N개
최대 B 개수
최소 W 개수

'''

n,b,w = map(int,input().split())

ls = list(input())

i = 0
j = 0

if ls[0] == 'B':
    b_cnt = 1
    w_cnt = 0
else:
    b_cnt = 0
    w_cnt = 1

result = 0

while i < n and j < n:
    # print(i,j,b_cnt,w_cnt)
    if b_cnt <= b and w_cnt >= w:
        result = max(result, j - i + 1)
        if j == n - 1:
            break
        j += 1
        if ls[j] == 'B':
            b_cnt += 1
        else:
            w_cnt += 1
    else: # 조건 충족 못했을 때
        if j == n - 1:
            break

        if w_cnt < w: # w충족이 안되면 늘려야함
            j += 1
            if ls[j] == 'B':
                b_cnt += 1
            else:
                w_cnt += 1
        if b_cnt > b: # 줄여야 함
            if ls[i] == 'B':
                b_cnt -= 1
            else:
                w_cnt -= 1
            i += 1

        if i > j:
            j += 1
            if ls[j] == 'B':
                b_cnt += 1
            else:
                w_cnt += 1


print(result)

'''
10 0 4
WWWWWWWWWW

10 1 1
BBBBBBBBBWB

'''