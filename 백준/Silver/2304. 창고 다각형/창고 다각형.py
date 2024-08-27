'''
창고 다각형

오목한 부분이 없게 -> 양끝에서부터 계속 높은 형태로

1. 가장 높은 것 기준까지 양끝에서 가운데로 모은다
2. 기준점의 앞뒤로 점화식 형식

'''


n = int(input())

dict = {}
max_h = 0
max_x = 0
for _ in range(n):
    x, h = map(int,input().split())
    max_h = max(h,max_h)
    max_x = max(x,max_x)
    dict[x] = h

prefix = [0]*(max_x+2)
middle = 0

for i in range(max_x+1):
    if i in dict.keys():
        if prefix[i-1] < dict[i]:
            prefix[i] = dict[i]
        else:
            prefix[i] = prefix[i-1]
    else:
        prefix[i] = prefix[i-1]

    if prefix[i] == max_h:
        middle = i
        break

for i in range(max_x,middle,-1):
    if i in dict.keys():
        if prefix[i+1] < dict[i]:
            prefix[i] = dict[i]
        else:
            prefix[i] = prefix[i+1]
    else:
        prefix[i] = prefix[i+1]

print(sum(prefix))