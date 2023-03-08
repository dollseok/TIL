# 백준 1654번 랜선 자르기

'''
길이가 제각각인 K개의 랜선을 가지고 있다
필요한 랜선 개수 N

가지고있는 랜선의 길이 K개만큼 주어짐

어떤 정수 A로 나누었을 때 몫이 N을 넘으면 만들 수 있는 것
K의 최소값부터 하나씩 생각
'''

K,N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

# print(lst)
sum_ = 0
res_list = []

mn = 1
mx = max(lst) + 1

while True:
    middle = (mn + mx) // 2
    for i in lst:
        sum_ += i//middle

    if sum_ >= N:
        if (sum_,mn,mx) in res_list:
            res = mn
            break
        res_list.append((sum_,mn,mx))
        mn = middle
        sum_ = 0

    else:
        if (sum_,mn,mx) in res_list:
            res = mx
            break
        mx = middle
        sum_ = 0


print(res)