'''

[H P S] 로 리스트에 입력 최대값이 무엇인지 지속적으로 확인

N은 최대 100000

주인공은 단 한번만 바꿀 것이다.
이때 최대로 이기는 횟수

P 냈을 때 이기는 횟수
H 냈을 때 이기는 횟수
S 냈을 때 이기는 횟수


H > S / S > P / P > H
'''


n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

prefix_H = [0]*(n)
prefix_S = [0]*(n)
prefix_P = [0]*(n)

for i in range(n):
    if arr[i] == 'H':
        prefix_P[i] += 1
    elif arr[i] =='S':
        prefix_H[i] += 1
    elif arr[i] == 'P':
        prefix_S[i] += 1

for i in range(1,n):
    prefix_H[i] = prefix_H[i-1] + prefix_H[i]
    prefix_S[i] = prefix_S[i-1] + prefix_S[i]
    prefix_P[i] = prefix_P[i-1] + prefix_P[i]


result = 0
for i in range(1,n):
    i_max = max([
        prefix_H[i] + prefix_P[n-1] - prefix_P[i],
        prefix_P[i] + prefix_H[n - 1] - prefix_H[i],
        prefix_H[i] + prefix_S[n - 1] - prefix_S[i],
        prefix_S[i] + prefix_H[n - 1] - prefix_H[i],
        prefix_S[i] + prefix_P[n - 1] - prefix_P[i],
        prefix_P[i] + prefix_S[n - 1] - prefix_S[i],
    ])
    # print(i)
    # print(prefix_H[i] - prefix_H[0] + prefix_P[n-1] - prefix_P[i],
    #     prefix_P[i] - prefix_P[0] + prefix_H[n - 1] - prefix_H[i],
    #     prefix_H[i] - prefix_H[0] + prefix_S[n - 1] - prefix_S[i],
    #     prefix_S[i] - prefix_S[0] + prefix_H[n - 1] - prefix_H[i],
    #     prefix_S[i] - prefix_S[0] + prefix_P[n - 1] - prefix_P[i],
    #     prefix_P[i] - prefix_P[0] + prefix_S[n - 1] - prefix_S[i])

    result = max(result,i_max)

print(result)