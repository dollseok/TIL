'''

G 킬로그램은 성원이의 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀것

G = 현재 몸무게 ** 2 - 기억 몸무게 ** 2
이것이 가능한 현재 몸무게

G < 100000

1 4 9 16 25 36 49 64 81 100 121
 3 5 7 9 11  13  15 17 19  21

       i
          j


제곱의 차이는 이렇게 진행됨 2씩 커짐 => 최소의 차이가 100000이 되려면?
-> 2n + 1 -> n이 50001까지

50002 * 50002

2500000000 => 25억 시간초과

투포인터

i = 0
j = 0


'''

G = int(input())
arr = []  # 제곱수들의 숫자 1차이 날때마다 차이의 값들
n = 50001

for i in range(1,n):
    arr.append(2*i + 1)

i = 0
j = 0
diff = arr[0]

result = []
while i < n-1 and j < n-1:

    if diff < G:
        j += 1
        diff += arr[j]
    elif diff > G:
        diff -= arr[i]
        i += 1
    else:
        result.append(j+2) # 위치는 두칸 뒤다.
        j += 1
        diff += arr[j]

if result == []:
    print(-1)
else:
    for k in result:
        print(k)