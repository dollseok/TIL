'''
연속합

1초 1억번

n개의 정수로 이루어진 임의의 수열
n 최대 100000

연속된 몇개의 수를 선택해서 구할수있는 합중에 가장 큰 합

풀이
1. 2차원 누적합으로 앞에서부터 안넣고 넣은 것, 이런 방식은 어때?

'''

n = int(input())
origin = list(map(int,input().split()))
ls = [0] + origin
prefix = [0] * (n+1)


for i in range(1,n+1):
    if prefix[i-1] + ls[i] > 0:
        prefix[i] = prefix[i - 1] + ls[i]
    else:
        prefix[i] = 0

if max(prefix) == 0:
    print(max(origin))
else:
    print(max(prefix))