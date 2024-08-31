'''

N 길이의 수열
연속된 수의 부분합 중 그 합이 S 이상 and 길이가 짧은 것

10 15

5 1 3 5 10 7 4 9 2 8

i=0, j=0에서 시작

찾으면 둘다 +1 +1
길이 짧은거 찾으면 결과값 길이 변경
'''

n,s = map(int,input().split())

ls = list(map(int,input().split()))

i = 0
j = 0

big = 100001
sum_ = ls[0]

result = big


while i < n and j < n:
    if j == n - 1 and sum_ < s:
        break
    if sum_ < s:
        j += 1
        sum_ += ls[j]
    elif sum_ >= s:
        result = min(result, j - i + 1)
        sum_ -= ls[i]
        i += 1

if result == big:
    print(0)
else:
    print(result)

