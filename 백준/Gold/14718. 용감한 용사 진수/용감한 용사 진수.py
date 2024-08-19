'''

힘 민첩 지능 3가지 능력치

1. 힘이 크거나 같고
2. 미첩이 크거나 같고
3. 지능이 크거나 같으면

이길수 있다.

용사 진수에게 최대한 많은 적을 이길수있도록 스탯포인트를 재분배
N명의 병사가 주어졌을 떄, K명의 병사를 이길수 있게하는 최소 스탯 포인트

N명 중에 K명 고르고 최소값

1. combi로 모든 경우의 수 체크
- combi => 메모리 초과

2. 힘,민첩,지혜 각 역할을 정해주는 것
최대 100*100*100 가지의 경우의 수의 조합
적군과 싸우는데 k명이 넘으면 result 최소값 비교 입력

'''


N,K = map(int,input().split())
str_list = []
dex_list = []
int_list = []
enemies = []

for _ in range(N):
    s,d,i = map(int,input().split())
    str_list.append(s)
    dex_list.append(d)
    int_list.append(i)
    enemies.append([s,d,i])

def check_win(user,enemies):
    cnt = 0
    for enemy in enemies:
        part_win = 0
        for t in range(3):
            if enemy[t] <= user[t]:
                part_win += 1

        if part_win == 3:
            cnt += 1

        if cnt == K:
            return True

    return False

result = 1000000*3

for i in range(N):
    for j in range(N):
        for k in range(N):
            user = [str_list[i],dex_list[j],int_list[k]]
            if check_win(user,enemies):
                result = min(result,sum(user))

print(result)