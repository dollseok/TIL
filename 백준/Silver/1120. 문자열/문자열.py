A,B = input().split()

diff = len(B) - len(A) + 1

result = 9999999999999999
for l in range(diff):
    cnt = 0
    new_string = ('X' *  l) +  A + ('X' * (diff - l))
    # print(new_string)
    for i in range(len(B)):
        if new_string[i] == 'X':
            continue
        if new_string[i] != B[i]:
            cnt += 1

    # print(cnt)
    result = min(cnt,result)

print(result)
