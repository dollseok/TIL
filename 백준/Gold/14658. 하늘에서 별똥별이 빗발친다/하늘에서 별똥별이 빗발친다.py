'''
N.M.L.K
N,M => 별똥별이 떨어지는 구역 가로 세로 길이
L => 트램펄린 한변의 길이
K => 별똥별의 수

L*L의 트램펄린을 준비, 지구 파괴를 막기 위해 별똥별에 떨어지는 것을 최소화
최대한 많은 별똥별을 튕겨내도록 배치했을 때 지구에는 몇개의 별동별이 떨어지나?
별똥별은 트램펄린의 모서리에 부딛혀도 튕겨나감

시간제한 2초 -> 2억번

K개의 별똥별 기준으로 4분면 => 그 안에 몇개의 별똥별이 들어있는지 최대 100개 한번 더 탐색

100 * 4 * 100

1. 풀이
각 꼭지점만있으면 되리라 생각했는데 다이아몬드처럼 배치가 되어있다면? => 불가

교점까지 해야할 것 같음


'''

N,M,L,K = map(int,input().split())

arr = []
check_point = []
x_list = []
y_list = []
for _ in range(K):
    a,b = map(int,input().split())
    x_list.append(a)
    y_list.append(b)
    arr.append([a,b])

for x in x_list:
    for y in y_list:
        check_point.append([x,y])

result = 101

dx = [L,L,-L,-L]
dy = [L,-L,-L,L]


for cx,cy in check_point:
    for i in range(4):
        cnt = 0
        for a, b in arr:
            min_x,max_x = sorted([cx,cx+dx[i]])
            min_y,max_y = sorted([cy,cy+dy[i]])
            if min_x <= a <= max_x and min_y <= b <= max_y:
                continue
            else:
                cnt += 1
        result = min(cnt,result)

print(result)
