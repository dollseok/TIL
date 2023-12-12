"""
이동하는 최소값
고장난 숫자로 만들수 있는 채널 리스트
앞의 숫자 + 숫자 개수 & 뒤의 숫자 + 숫자 개수 = 버튼 클릭수 중 작은것


2. 시간 복잡도
채널 숫자 수 N 최대 500000 -> 6자리수
버튼 수 최대 10
O( 10*6 + 10*6 리스트 순회 )



3. 필요한 것
목표 채널 숫자
가지고 있는 숫자로 만들수 있는 숫자 리스트

"""

import sys
input = sys.stdin.readline

target = input().strip()
N = int(input())
broken = list(map(int, input().split()))

min_count = abs(100-int(target))

for i in range(1000001):
    num = str(i)

    if len(num) > len(target) + 1:
        break
    for j in range(len(num)):
        if int(num[j]) in broken:
            break
        elif j == len(num)-1:
            min_count = min(abs(i-int(target))+len(num),min_count)

print(min_count)
