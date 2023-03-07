# Baekjoon 2564번 경비원

'''
블록의 가로 세로
상점의 개수


'''

def place_maker(pl):     # place가 들어오면
    if pl == 1:
        le = 4
        ri = 3
        oth = 2
    elif pl == 2:
        le = 3
        ri = 4
        oth = 1
    elif pl == 3:
        le = 1
        ri = 2
        oth = 4
    elif pl == 4:
        le = 2
        ri = 1
        oth = 3
    return [le, ri, oth]

w, l = map(int,input().split())
N = int(input())

data = [list(map(int,input().split())) for _ in range(N+1)]
s,d = data.pop()     # 동근이 위치, 거리
# 2, 3
left, right, other = place_maker(s)
sum_ = 0

if s == 1:
    for i in range(N):
        market, market_d = data[i]
        if market == s:
            sum_ += abs(d - market_d)
        elif market == other:
            sum_ += min([(market_d + d), 2*w - (market_d + d)]) + l
        elif market == left:
            sum_ += (w - d) + market_d
        elif market == right:
            sum_ += d + market_d

elif s == 2:
    for i in range(N):
        market, market_d = data[i]
        if market == 3 or market == 4:
            market_d = l - market_d

        if market == s:
            sum_ += abs(d - market_d)
        elif market == other:
            sum_ += min([(market_d + d), 2*w - (market_d + d)]) + l
        elif market == left:
            sum_ += market_d + d
        elif market == right:
            sum_ += market_d + w - d

elif s == 3:
    for i in range(N):
        market, market_d = data[i]
        if market == s:
            sum_ += abs(d - market_d)
        elif market == other:
            sum_ += min([(market_d + d), 2 * l - (market_d + d)]) + w
        elif market == left:
            sum_ += d + market_d
        elif market == right:
            sum_ += (l - d) + market_d

elif s == 4:
    for i in range(N):
        market, market_d = data[i]
        if market == 1 or market == 2:
            market_d = w - market_d

        if market == s:
            sum_ += abs(d - market_d)
        elif market == other:
            sum_ += min([(market_d + d), 2 * l - (market_d + d)]) + w
        elif market == left:
            sum_ += l - d + market_d
        elif market == right:
            sum_ += d + market_d

print(sum_)