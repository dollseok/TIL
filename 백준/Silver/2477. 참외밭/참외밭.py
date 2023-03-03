N = int(input())      # 1m^2에 자라는 참외 개수
spot_list = [list(map(int, input().split())) for i in range(6)]
# print(spot_list)      # [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]

mx_col = 0
mx_row = 0
col_idx = 0
row_idx = 0

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
except_list = [col_idx,row_idx]

if (col_idx + 1) % 6 == row_idx:      # col_idx 뒤에 row_idx가 있다면
    except_list.append((6 + col_idx - 1) % 6)
    except_list.append((row_idx + 1) % 6)

else:                                 # col_idx 앞에 row_idx가 있다면
    except_list.append((6 + row_idx - 1) % 6)
    except_list.append((col_idx + 1) % 6)

# 얘네만 제외하면 됨
# print(except_list)
part_idx = []

for i in range(6):
    if i not in except_list:
        part_idx.append(i)

res = (mx_col*mx_row - spot_list[part_idx[0]][1]*spot_list[part_idx[1]][1])*N

print(res)