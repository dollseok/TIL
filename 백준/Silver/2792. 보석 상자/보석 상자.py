'''

M가지 서로 다른 색상의 보석
모든 보석을 N명의 학생들에게 나누어 줌

N,M

5 2
7
4

RRRR BBBBBBB

5명에게 나누어줌
총 11개

질투심이 m일 때, N명에게 나누어줄 수 있는지 여부를 확인

'''

n,m = map(int,input().split())
ls = []
for _ in range(m):
    ls.append(int(input()))

low = 1 # 최소 1부터 시작해야함
high = max(ls)
result = 10e9 + 1
mid = (low+high) // 2
while low <= high:
    mid = (low+high) // 2
    tot = 0

    for jem in ls:
        if jem % mid == 0:
           tot += jem // mid
        else:
            tot += jem // mid + 1

    # print(low, high, mid, tot)

    if tot <= n: # 나눠지는 최소 인원 수가 n보다 작으면 더 작은 수로 나눠야함 => high를 줄임
        high = mid - 1
        result = min(result,mid)
    elif tot > n: # 나눠지는 최소 인원 수가 n 보다 크면 더 큰수로 나눠야 함
        low = mid + 1



print(result)
'''
7 5
1
1
1
1
1
'''