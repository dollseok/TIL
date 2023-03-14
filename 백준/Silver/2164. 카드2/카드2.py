# 백준 2164번 카드2

'''
N장의 카드
1번 제일 위, N번 이 제일 아래

제일 위는 버리고 그다음 카드는 제일 아래로 옮김
마지막 한장 프린트
'''

# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
cards = []

for i in range(1,N+1):
    cards.append(i)


while len(cards) != 1:
    if len(cards)%2 == 1:
        new_cards=[]
        for i in range(len(cards)):
            if i % 2 == 1:
                new_cards.append(cards[i])
        cards = new_cards + [new_cards.pop(0)]

    else:
        new_cards = []
        for i in range(len(cards)):
            if i % 2 == 1:
                new_cards.append(cards[i])
        cards = new_cards


print(*cards)

