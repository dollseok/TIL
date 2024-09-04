'''
N개의 카드, 정수 M 개

숫자카드를 상근이가 가자고있는지 아닌지 구하는 프로그램

N : 500000

M = -10000000 ~ 10000000

M개의 수에 대해서 상근이가 가진 N개의 숫자가 있는지 각각 판별

-10 2 3 6 10
s
           e
      s             2
           e        4
         s          3
           e        4   7//2 = 3

'''

M = int(input())

ls = sorted(list(map(int,input().split())))

N = int(input())
cards = list(map(int,input().split()))
res = []
for i in range(N):
    s = 0
    e = M-1
    target = cards[i]
    result = 0
    while s <= e:
        mid = (s+e)//2
        if ls[mid] == target:
            result = 1
            break
        elif ls[mid] > target:
            e = mid - 1
        else:
            s = mid + 1

    res.append(result)

print(*res)