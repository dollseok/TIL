# Baekjoon 2477번 참외밭

'''
가장 긴 것은 두개가 붙어있다, 그 둘 합친 것의 양끝을 지운다
가장 긴 것에 붙어있는 짧은 길이를 찾는게 핵심

처음에는 모양이 한정되어있어서 가는 모양에 따라서 if문 처리를 하려고했지만 제외해야할 것이 너무 많았음
'''

# import sys
# sys.stdin = open('input.txt','r')

N = int(input())        # 1m^2에 자라는 참외 개수
spot_list = [list(map(int, input().split())) for i in range(6)]
# print(spot_list)      # [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]

mx_col = 0
mx_row = 0
col_idx = 0
row_idx = 0

# [1] spot_list에서 col,row에 대해서 가장 긴 값과 그 인덱스를 추출
for i in range(6):
    if spot_list[i][0] == 4 or spot_list[i][0] == 3:
        if mx_col < spot_list[i][1]:
            mx_col = spot_list[i][1]
            col_idx = i

    elif spot_list[i][0] == 1 or spot_list[i][0] == 2:
        if mx_row < spot_list[i][1]:
            mx_row = spot_list[i][1]
            row_idx = i

# print(mx_col,mx_row, col_idx, row_idx)         # 50 160 0 1

# [2] 제외할 인덱스 리스트를 생성한 후에 거기에 각각 붙어있는 짧은 변의 인덱스 추출
except_list = [col_idx,row_idx]                  # 제외할 인덱스 리스트

if (col_idx + 1) % 6 == row_idx:                 # col_idx 뒤에 row_idx가 있다면
    except_list.append((6 + col_idx - 1) % 6)    # col 앞에 있는 것이 part가 아닌 부분
    except_list.append((row_idx + 1) % 6)        # row 뒤에 있는 것이 part가 아닌 부분

else:                                            # col_idx 앞에 row_idx가 있다면
    except_list.append((6 + row_idx - 1) % 6)    # row 앞에 있는 것이 part가 아닌 부분
    except_list.append((col_idx + 1) % 6)        # col 뒤에 있는 것이 part가 아닌 부분

# 얘네만 제외하면 됨
# print(except_list)       # [0, 1, 5, 2]

part_idx = []                     # 파트의 인덱스를 모을 리스트
for i in range(6):                # 제외리스트에 없는 인덱스를 하나씩 뽑아서 part_idx 에 추가
    if i not in except_list:
        part_idx.append(i)

res = (mx_col*mx_row - spot_list[part_idx[0]][1]*spot_list[part_idx[1]][1])*N

print(res)
