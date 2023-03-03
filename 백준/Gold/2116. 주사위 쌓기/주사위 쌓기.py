def remove_center(dice_list, bottom):
    global res,N
    side_max = 0
    for i in range(N):                   # 다이스의 각각 확인
        idx = dice_list[i].index(bottom)
        if idx == 0:
            rev_idx = 5
        elif idx == 1:
            rev_idx = 3
        elif idx == 2:
            rev_idx = 4
        elif idx == 3:
            rev_idx = 1
        elif idx == 4:
            rev_idx = 2
        elif idx == 5:
            rev_idx = 0

        bottom = dice_list[i][rev_idx]
        side_dice_list = []
        except_idx = [idx, rev_idx]
        for j in range(6):
            if j not in except_idx:
                side_dice_list.append(dice_list[i][j])

        side_max += max(side_dice_list)



    res = max([side_max,res])




N = int(input())      # 주사위의 개수

dice_list = [list(map(int,input().split())) for _ in range(N)]

res = 0

for i in range(6):      # 각 여섯면에 대해서 확인
    bottom = dice_list[0][i]  # 첫번째 면

    remove_center(dice_list, bottom)

    # print(dice_list)

print(res)
