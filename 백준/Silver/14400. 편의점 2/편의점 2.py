'''
거리 최소값

x,y 좌표의 편의점 위치들
x축 기준 좌우로 이동할 때 중간 값이 최소값
y축 기준 좌우로 이동할 때 중간 값이 최소값

x축의 중앙값 , y축의 중앙값

'''

n = int(input())
x_list = []
y_list = []
for _ in range(n):

    a,b = map(int,input().split())

    x_list.append(a)
    y_list.append(b)

x_list.sort()
y_list.sort()

middle = []
result = 0
if n % 2 == 0:
    middle = [x_list[n//2-1], y_list[n//2-1]]
else:
    middle = [x_list[n//2], y_list[n//2]]

for i in range(n):
    result += abs(x_list[i] - middle[0])
    result += abs(y_list[i] - middle[1])

print(result)