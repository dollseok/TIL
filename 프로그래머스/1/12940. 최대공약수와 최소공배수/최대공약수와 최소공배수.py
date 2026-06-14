def solution(n, m):
    a, b = n, m

    # 최대공약수 구하기: 유클리드 호제법
    while b != 0:
        a, b = b, a % b

    gcd = a
    lcm = n * m // gcd

    return [gcd, lcm]