N, X = map(int,input().split())

visits = list(map(int,input().split()))

current_sum = sum(visits[0:X])
max_sum = current_sum
max_cnt = 1

for i in range(1, N-X+1):
    #print(current_sum, max_sum)
    current_sum = current_sum - visits[i-1] + visits[i+X-1]
    
    if current_sum > max_sum:
        max_sum = current_sum
        max_cnt = 1
    elif current_sum == max_sum:
        max_cnt += 1


if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(max_cnt)    
    