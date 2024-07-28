'''
삼각수 다 만들어서 세개를 골라서 더해서 최종 리스트에 추가
'''

t = int(input())

size = 1
cnt = 2
triangle_list = [1]
while True:
    size = size + cnt
    cnt += 1

    if size > 1000:
        break

    triangle_list.append(size)

l = len(triangle_list)
result_set = set([])

for i in range(l):
    for j in range(l):
        for k in range(l):
            result_set.add(triangle_list[i] + triangle_list[j] + triangle_list[k])


for _ in range(t):
    k = int(input())
    if k in result_set:
        print(1)
    else:
        print(0)