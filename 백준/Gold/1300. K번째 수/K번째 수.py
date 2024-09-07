'''
배열의 N*N
A[i][j] = i * j

일차원 배열 B에 넣음 => 오름차순 정렬했을 때 B[k]의 값

N <= 100000

이 배열안에 잇는 숫자인지 어떻게 판별할 것인가?



'''

n = int(input())

k = int(input())



# 숫자를 모두 구할 필요가 없음. 개수만 세면됨
# ls = [[0] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         ls[i][j] = (i+1)*(j+1)

# for p in ls:
#     print(p)

s = 1
e = k # k번째 수를 구하기 위해서 최대는 k 이하 일것
mid = (s+e)//2
result = 0
while s <= e:
    tot = 0
    mid = (s+e)//2

    for i in range(1,n+1):
        tot += min(mid//i,n) # 이부분이 메인이다.

    # 개수를 세는 방식에 대해서
    # mid 숫자 보다 작은 개수를 세려면 각 행별로 그 i번째 행의 수를 나눠주면 편하게 계산 가능
    # ex) 5,20 이 입력
    # 첫 mid = 10
    # 10 // 1 => 10 첫번째 행에서는 모두 10보다 작으므로 N개가 선택
    # 10 // 2 => 5 두번째 행에서는 모두 10 // 2 보다 작은것이 2 4 6 8 10 5개
    # 10 // 3 => 3 세번째 행에서는 10 보다 작은 수가 3개
    # 10 // 4 => 2 네번째 행에서는 10보다 작은 수가 2개
    # 10 // 5 => 2 다섯번째 행에서는 10보다 작은수가 2개

    # print(s, e, tot, mid)

    if tot >= k:
        result = mid
        e = mid - 1

    else:
        s = mid + 1

print(result)
