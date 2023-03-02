N1 = int(input())
mx_len = 0
for N2 in range(1, N1+1):                        # N2 두번째수
    N3 = N1 - N2
    num_list = [N1, N2, N3]                      # 미리 초반 세 수는 추가해둠
    while True:
        new_num = num_list[-2] - num_list[-1]    # 앞앞 수랑 앞 수랑 뺀 수가 새로운 수
        if new_num < 0:
            break
        num_list.append(new_num)

    if mx_len < len(num_list):
        mx_len = len(num_list)
        res = num_list

print(mx_len)
print(*res)