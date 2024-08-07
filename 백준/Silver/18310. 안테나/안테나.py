'''

집의 수 N
1 <= N <=200000

집의 위치가 1이상 100000이하의 자연수로 주어진다.

4
5 1 7 9

0 0 0 0 0 0 0 0 0
1       5   7   9   위치
0       4   6   8  / 1  : 18
1       3   5   7  / 2  : 16
2       2   4   6  / 3  : 14
3       1   3   5  / 4  : 12
4       0   2   4  / 5  : 10
5       1   1   3  / 6  : 10
6       2   0   2  / 7  : 10
7       3   1   1  / 8  : 12
8       4   2   0  / 9  : 14

1. 모든 점 확인 => 200000개의 집 / 집 위치의 종류는 최대 100000 => 100000*200000  => 시간 초과나 날수 밖에 없음
2. 이동하는데 중간 지점으로 갈수록 줄어들고 중간에서 멀어질수록 늘어난다 => 중간 지점이 최소값

'''

N = int(input())
l = list(map(int,input().split()))

l.sort()

if N%2 == 0:
    print(l[N//2-1])
else:
    print(l[N//2])


# res = [9999999999,0]
# for i in range(1,100001):
#     dist = 0
#     for house in l:
#         dist += abs(house-i)
#
#     if res[0] <= dist:
#         print(res[1])
#         break
#     else:
#         res = [dist,i]