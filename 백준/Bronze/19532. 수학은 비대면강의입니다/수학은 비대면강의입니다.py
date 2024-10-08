'''

완전 탐색은 값을 모두 다 넣어보는 것이다
이 과정에서 시간을 생각해보고 최적화 된 방향을 생각해야한다.
=> 여기에서 쓰이는 것이 알고리즘

연립 방정식 => 해가 x,y 인데 각각 -999, 999이하인 정수인 경우만 입력 주어짐 보장

- 완전 탐색
2000 * 2000 x,y 의 모든 경우를 모두 돌렸을 때 => 4000000의 경우의 수 => 1초 (1억번) 이하

- 만약에 진짜 연립 방정식으로 구하는 것은 비효율 적일까?
컴퓨터적인 계산이 아닌 손풀이 계산이 되어버릴 것
공식 생성해서 푸는 방식 => 바로 계산이 되어나오니 빠르긴 할듯

'''

a,b,c,d,e,f = map(int,input().split())

def check_result():
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                return [x, y]

print(*check_result())