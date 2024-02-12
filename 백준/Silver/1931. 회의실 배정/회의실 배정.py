'''
1. 끝나는 시간이 빨라야 다음 회의가 빨리 시작할 수 있다
2. 같거나 같아야 다음에 시작할 수 있다

& 시작시간도 고려해야한다.
반례

3
4 4
3 4
2 4
---
2
'''

n = int(input())
arr = []

for _ in range(n):
    s,e = map(int,input().split())
    arr.append((s,e))

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

cnt = 0
end_point = 0
for i in arr:
    if i[0] >= end_point:
        cnt += 1
        end_point = i[1]

print(cnt)