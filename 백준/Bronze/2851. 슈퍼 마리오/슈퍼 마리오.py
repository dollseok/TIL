'''
슈퍼마리오

중간에 버섯을 먹는 것을 중단했다면 이후에 나온 버섯은 모두 먹을 수 없다.

- 연속적으로만 먹을수 있다.
- 처음것을 못먹으면 아예 못먹는 것

1. 완전탐색
총 10개의 줄
0부터 끝
0부터 끝 -1
0부터 끝 -2 ...
모두 구한 후에 100에 가까운 것을 고름

2. 0부터 계속더하다가 100넘으면 바로 앞과 뒤에거 중에 100에 가까운 값을 출력

'''

list = []
for i in range(10):
    list.append(int(input()))

current = 0
for j in list:
    if current + j >= 100:
        if (current + j - 100) <= (100 - current):
             current += j
        break
    else:
        current += j

print(current)