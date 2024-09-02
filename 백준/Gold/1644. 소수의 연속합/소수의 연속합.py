'''

연속된 소수의 합으로 경우의 수를 구할 수 있는 프로그램

1 ~ 4000000 까지 올라가며 각 숫자가 소수인지 판단하고 더해보면서 최종값에 도달하는지 확인
만약 넘어간다면 앞에것을 제외하고 추가로 더하는 방식
소수인지 어떻게 판별하지? -> 에라토스테네스의 체

'''

def isPrime(n):
    end = int(n ** 0.5)
    for i in range(2,end+1):
        if n % i == 0:
            return False

    return True

n = int(input())

s = 0
e = 0

arr = []
if n == 1:
    print(0)
else:
    for i in range(2,n+1):
        if isPrime(i):
            arr.append(i)

    tot = arr[0]
    cnt = 0
    while s < len(arr)-1 and e < len(arr)-1:
        if tot < n:
            e += 1
            tot += arr[e]
        elif tot > n:
            tot -= arr[s]
            s += 1
        else:
            cnt += 1
            tot -= arr[s]
            s += 1

    if isPrime(n):
        cnt += 1

    print(cnt)