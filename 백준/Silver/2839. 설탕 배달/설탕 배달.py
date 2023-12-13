import sys
input = sys.stdin.readline

"""
사탕가게 N키로 배달 3kg 5kg 두개 있음
최대한 적은 봉지
N킬로 정확히 못만들면 -1
"""

N = int(input())
res = 100000
cnt5 = 0

for cnt3 in range(N//3+1):
    if (N-3*cnt3) % 5 == 0:
        cnt5 = (N-3*cnt3)//5
        res = min(cnt3 + cnt5, res)

if res == 100000:
    res = -1

print(res)
