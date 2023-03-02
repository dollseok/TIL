T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())        # N : 사람수, M : 만드는데 걸리는 시간, K개 붕어빵 제작
    person_time = list(map(int, input().split()))    # N개 만큼 있다.

    bread_timeline = [0]*(max(person_time)+1)       # 인덱스 사용할 것

    res = 'Possible'

    for i in range(len(bread_timeline)):
        bread_timeline[i] += bread_timeline[i-1]

        if i % M == 0 and i != 0:
            bread_timeline[i] += K

        if i in person_time:
            bread_timeline[i] -= person_time.count(i)
            if bread_timeline[i] <= -1:
                res = 'Impossible'
                break

    print(f'#{test_case}', res)
