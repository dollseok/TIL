'''
숫자 야구

자리와 숫자가 맞으면 스트라이크
숫자만 맞으면 볼
3스트라이크면 게임 끝


1.
모든 숫자는 총 111 ~ 999 -> 세자리 중 가장 작은 숫자 ~ 가장 큰숫자 => 1000이하
질문 개수는 최대 100개
질문1 에서 123과 조건에 맞는 숫자만 킵, 나머지 제외 => 1000 * 100 -> 100,000 계산 여기에 각 계산 마다 자리 별로 확인하는 3 => 1초 이하
=> 111 ~ 999 숫자리스트 만들어서 각조건 확인

2.
123 에서 1스트라이크 1볼인 경우의수 빼놓기 => 첫 조건에서 많이 빠짐
그중에 356중에 1스트라이크 1볼인 경우의 수 빼기

'''

N = int(input())

cnt_list = [0]*1001 # 인덱스로 개수 체크


for _ in range(N):
    n,s,b = map(int, input().split())

    for i in range(111,1000):
        candi = list(str(i))
        check = list(str(n))
        strike_cnt = 0
        ball_cnt = 0
        if len(set(candi)) == 3 and '0' not in candi: # 중복된 것 없을때만 검사
            for j in range(3):
                if candi[j] == check[j]:
                    strike_cnt += 1
                elif candi[j] in check:
                    ball_cnt += 1
            if ball_cnt == b and strike_cnt == s:
                cnt_list[i] += 1

result = 0
for c in cnt_list:
    if c == N:
        result += 1

print(result)

