'''

12842번 튀김소보루

n,s
1000 975
첫 소보루개수, 남아있던 소보루 개수

명의 인원수
1~m 번까지의 사람이 한개 소보루 먹는데 걸리는 시간 t 초

3
1
3
5

25개를 먹은 것

1 2 3 4 5 6 7

1초  2초  3초  4초  5초  6초 7초 8초 9초 10초 11초
1    1   1    1   1    1   1   1   1   1   1
3             3            3           3
5                      5                   5


n-s개를 먹은 것

가장 많은 시간초인 사람부터 몇개를 먹고 -> 그사람 열외


m이 10만개


'''

n,s = map(int,input().split())
m = int(input())
time = [int(input()) for _ in range(m)]

t = 0
while n != s:
    for i in range(m):
        if t % time[i] == 0:
            n -= 1
            if n == s:
                print(i+1)
                break

    t += 1


