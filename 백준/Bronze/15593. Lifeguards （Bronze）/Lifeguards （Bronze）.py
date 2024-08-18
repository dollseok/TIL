'''

t가 0 ~ 1000 시간 사이에 오픈한다

라이프 가드를 뽑았는데 n명을 봅앗고 각 시작시간과 끝나는 시간이 주어진다 => 4-7이면 3포인트 만큼 커버하는 것
한명을 해고시켜야한다.

한명 해고했을 대 커버할수있는 최대 시간

N 최대 100
t 는 1- 1000


- 완전 탐색
100*1000을 해서 전체 리스트를 구한 후에
100번을 더 돌려서 빼고 카운트 확인
2초라 충분히 가능할 것 같음

- 풀다보니 백트래킹 같음
'''

time_table = [0] * 1001

n = int(input())

arr = []
start = 1001
end = 0

for _ in range(n):
    s,e = map(int,input().split())
    start = min(s,e,start)
    end = max(s,e,end)
    arr.append([s,e])

    for i in range(s,e):
        time_table[i] += 1


result = 0
for cs,ce in arr:
    cnt = 0
    for j in range(cs,ce):
        time_table[j] -= 1

    for k in range(start,end):
        if time_table[k] > 0:
            cnt += 1

    for t in range(cs, ce):
        time_table[t] += 1

    result = max(cnt,result)

print(result)

