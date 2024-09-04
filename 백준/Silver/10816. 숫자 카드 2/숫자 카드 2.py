'''

12 => 3
-10 -10 2 3 3 6 7 10 10 10 10 10
s                                  0
                               e   9  => 4
                 m                 m > t
s
                 e
          m



'''

N = int(input())
ls = sorted(list(map(int,input().split())))

M = int(input())
cards = list(map(int,input().split()))

res = []
for i in range(M):
    s = 0
    e = N - 1

    left = 0
    right = N-1
    target = cards[i]
    # 오른쪽 찾기
    while s <= e:
        mid = (s + e) // 2
        if ls[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    right = e

    # 왼쪽 찾기
    s = 0
    e = N - 1
    while s <= e:
        mid = (s + e) // 2
        if ls[mid] < target:
            s = mid + 1
        else:
            e = mid - 1

    left = s

    res.append(right - left + 1)

print(*res)