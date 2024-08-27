'''
나는 정말 휘파람을 못불어

1초
N <= 200000
S 대문자 문자열

WH 가 앞에 있고 -> 뒤에 E의 개수
WHEE 모양이 되는 부분 수열의 개수

H 기준으로 앞의 W 뒤의 E를 생각

'''


n = int(input())

ls = list(input())

prefix_w =[0]*n
prefix_e =[0]*n

for i in range(n):
    if ls[i] == 'W':
        prefix_w[i] += 1
    elif ls[i] == 'E':
        prefix_e[i] += 1

for i in range(1,n):
    prefix_w[i] += prefix_w[i-1]
    prefix_e[i] += prefix_e[i-1]

cnt = 0
for i in range(1,n):
    if ls[i] == 'H':
        eCnt = prefix_e[n-1] - prefix_e[i]
        cnt += (prefix_w[i-1]) * (2**eCnt - eCnt - 1)

print(cnt % 1000000007)