# 백준 1654번 랜선 자르기

'''
길이가 제각각인 K개의 랜선을 가지고 있다
필요한 랜선 개수 N

가지고있는 랜선의 길이 K개만큼 주어짐

어떤 정수 A로 나누었을 때 몫이 N을 넘으면 만들 수 있는 것
K의 최소값부터 하나씩 생각
'''

'''
내가 계속 틀린 이유
mx = max(lst) + 1
이 부분에서 마지막 값도 봐야하는데 +1을 안해주면 마지막 것을 확인을 못해보는 것
이진 탐색으로 풀어야함

'''

# import sys
# sys.stdin = open('input.txt', 'r')

K,N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

# print(lst)
sum_ = 0
res_list = []

mn = 1
mx = max(lst) + 1

while True:
    middle = (mn + mx) // 2     # 가장 큰값+1 과 1의 중간을 탐색
    for i in lst:
        sum_ += i//middle       # 몫의 합들을 구함

    if sum_ >= N:                      # 자른 랜선의 개수가 N보다 크면
        if (sum_,mn,mx) in res_list:   # 튜플로 만든 값이 이미 결과에 있으면
            res = mn                   # 아래에서 부터 올라오면서 찾았으므로 결과는 mn
            break
        res_list.append((sum_,mn,mx))  # 합, 최소값, 최대값을 튜플로 결과 리스트에 넣음
        mn = middle
        sum_ = 0

    else:                              # 자른 랜선의 개수가 N보다 작으면
        if (sum_,mn,mx) in res_list:   # 튜플로 만든 값이 이미 결과에 있으면
            res = mx                   # 위에서부터 내려오면서 찾았으므로 결과는 mx
            break
        mx = middle                    # N보다 작은건 결과가 아님으로 결과에 추가하진 않음
        sum_ = 0


print(res)