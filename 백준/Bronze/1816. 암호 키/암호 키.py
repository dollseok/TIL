'''
2초 시간 제한

10^6 보다 큰 소수이면 매우 큰 소수
소수인지 아닌 지 확인해야함 10^6 보다 작은 수에서 나눠지면 비밀번호로 적합 x

'''

N = int(input())

for _ in range(N):
    result = ''
    password = int(input())
    for i in range(2,1000001):
        if password % i == 0:
            result = 'NO'
            break
        else:
            result = 'YES'

    print(result)