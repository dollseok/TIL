'''
1043번 거짓말

bfs 응용
'''
from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
connection_list = [[]*(n+1)] # 모르면 False 알면 True
visited = [False] * (n+1)

know_people = deque(map(int,input().split()))
know_people_cnt = know_people.popleft()

party_list = []

for i in range(m):
    party_people = deque(map(int,input().split()))
    party_people_cnt = party_people.popleft()
    party_list.append(party_people)

while know_people:
    p = know_people.popleft()
    visited[p] = True
    for party in party_list:
        if p in party: # 아는 사람이 그 파티에 있으면
            for i in party: # 파티에 모든 사람을 아는 사람으로 추가
                if not visited[i]:
                    know_people.append(i)

# 이렇게하면 만나면 안되는 사람이 모두 정해진 것

# 각 파티에 진실을 아는 사람이 있는지 체크
result = 0
for party in party_list:
    bad_party = False
    for i in party:
        if visited[i]:
            bad_party = True
            break

    if not bad_party:
        result += 1

print(result)